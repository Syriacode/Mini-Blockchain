# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A step-by-step blockchain learning series: each numbered directory (`01-simple-chain`, `02-stablecoin`, ...) is a self-contained project. The user is learning, so explain changes and reasoning instead of only producing code. Later projects reference fixes for earlier ones' "known simplifications" (for example, P01's exercises point to Project 02 for authorization and Project 04 for networking/consensus), so keep each project's scope as its README describes it.

**Always run the relevant tests after changing code** (`python -m pytest` for 01, `forge test` for 02), and show the output. A change isn't done until its tests pass.

## Project 01 — simple chain (Python, no dependencies besides pytest)

```bash
cd 01-simple-chain
python demo.py                                   # mine, check balances, tamper with history
python -m pytest -v                              # all tests
python -m pytest -v test_blockchain.py::test_mining_rewards_the_miner   # single test
```

All logic is in `blockchain.py`: a `Block` dataclass (SHA-256 over every field except `hash`, JSON with `sort_keys`) and `Blockchain` (proof-of-work `_mine`, `add_transaction`, `mine_pending`, `balance_of`, `is_valid`). Balances come from replaying all transactions, minus pending outgoing ones, which prevents double-spends. Mining rewards come from the `NETWORK` sender. Tests use `difficulty=2` to stay fast. The simplifications (no signatures, floats for amounts, no networking) are intentional.

## Project 02 — mintable stablecoin (Solidity / Foundry) — in progress

`02-stablecoin` is a Foundry/Solidity project (forge, anvil, cast). Currently only `02-stablecoin/GUIDE.md` exists. It's an 8-step plan, and each step has Learn / Prompt / You check / Done when / Commit sections. When working on a step, follow the guide's prompt and use its exact commit message. Leave the "You check" verification to the user and point them to it. Don't skip ahead to later steps.

Setup choices the guide fixes (Step 1):
- The repo root is the only git repo. Scaffold with `forge init --force --no-git .` inside `02-stablecoin`. Dependencies are git submodules, recorded in the **root** `.gitmodules`: `forge-std` and `openzeppelin-contracts-upgradeable`.
- `remappings.txt`: `@openzeppelin/contracts-upgradeable/` → `lib/openzeppelin-contracts-upgradeable/contracts/`, `@openzeppelin/contracts/` → `lib/openzeppelin-contracts-upgradeable/lib/openzeppelin-contracts/contracts/`, `forge-std/` → `lib/forge-std/src/`.

Commands (run from `02-stablecoin`):
```bash
forge build
forge test -vv
forge test --match-test <name> -vvv            # single test
forge test --match-contract <Contract>
forge fmt            # CI runs: forge fmt --check, forge build --sizes, forge test -vvv
forge coverage --report summary
anvil                # local chain (Step 7); deploy with forge script, interact with cast
```

Contract design to preserve (`src/StableCoin.sol`):
- UUPS upgradeable, deployed behind an `ERC1967Proxy`, set up by `initialize` (no constructor logic). `_authorizeUpgrade` is restricted to `onlyRole(UPGRADER_ROLE)`.
- **6 decimals** (USDC-style): $1 = `1_000_000`.
- Roles: `DEFAULT_ADMIN_ROLE` (grants roles, sets minter allowances), `MINTER_ROLE` (mints up to its allowance, burns its own balance), `PAUSER_ROLE`, `BLOCKLISTER_ROLE`, `UPGRADER_ROLE`. Even the admin can't upgrade without `UPGRADER_ROLE`.
- Custom state lives in an **ERC-7201 namespaced storage struct** (`StableCoinStorage`). Append new fields only. Never reorder fields or add top-level state variables, because that corrupts storage across upgrades.
- Pause and blocklist checks go in the `_update` override, which every transfer, mint, and burn passes through. It checks `from`, `to`, **and `msg.sender`** (this blocks `transferFrom` by a blocklisted spender).
- Use custom errors (`ZeroAddress`, `AccountBlocklisted`, ...), not revert strings.

Testing pitfall: `vm.prank` applies to the *next external call*, and that includes a getter such as `coin.MINTER_ROLE()` inside `vm.expectRevert(...)`. Read role constants into local variables **before** calling `vm.prank`.

Keys: read deploy keys from environment variables. `.env` is gitignored, so never commit keys.

## Environment

The machine runs Windows. The guide's shell commands (`rm -rf`, etc.) are POSIX, so run them with the Bash tool.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A step-by-step blockchain learning series: each numbered directory (`01-simple-chain`, ...) is a self-contained project. The user is learning, so explain changes and reasoning instead of only producing code. Later projects reference fixes for earlier ones' "known simplifications" (for example, P01's exercises point to Project 02 for authorization and Project 04 for networking/consensus), so keep each project's scope as its README describes it.

**Always run the relevant tests after changing code** (`python -m pytest` for 01), and show the output. A change isn't done until its tests pass.

## Project 01 — simple chain (Python, no dependencies besides pytest)

```bash
cd 01-simple-chain
python demo.py                                   # mine, check balances, tamper with history
python -m pytest -v                              # all tests
python -m pytest -v test_blockchain.py::test_mining_rewards_the_miner   # single test
```

All logic is in `blockchain.py`: a `Block` dataclass (SHA-256 over every field except `hash`, JSON with `sort_keys`) and `Blockchain` (proof-of-work `_mine`, `add_transaction`, `mine_pending`, `balance_of`, `is_valid`). Balances come from replaying all transactions, minus pending outgoing ones, which prevents double-spends. Mining rewards come from the `NETWORK` sender. Tests use `difficulty=2` to stay fast. The simplifications (no signatures, floats for amounts, no networking) are intentional.

## Project 02 — moved

The stablecoin project now lives in its own repository, https://github.com/Syriacode/upgradeable-stablecoin
(full history preserved). Don't recreate a `02-stablecoin` folder here.

## Environment

The machine runs Windows. Shell commands in the docs are POSIX, so run them with the Bash tool.

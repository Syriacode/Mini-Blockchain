# Mini-Blockchain

A step-by-step series of blockchain projects built while learning Claude Code.
Each folder is a self-contained project that adds one new concept.

| # | Project | Concepts | Status |
|---|---------|----------|--------|
| 01 | [Simple chain](01-simple-chain) | Blocks, SHA-256, proof-of-work, validation, balances | ✅ |
| 02 | Signed transactions | ECDSA keys, wallets, digital signatures | ⏳ |
| 03 | Merkle trees | Merkle roots, inclusion proofs | ⏳ |
| 04 | P2P network | Flask REST API, multiple nodes, longest-chain consensus | ⏳ |
| 05 | First smart contract | Solidity, Hardhat, tests, local deploy | ⏳ |
| 06 | ERC-20 token | OpenZeppelin, allowances, events | ⏳ |
| 07 | dApp front end | ethers.js, MetaMask, testnet deploy | ⏳ |

## Run a project

```bash
cd 01-simple-chain
pip install pytest
python demo.py
python -m pytest -v
```

## How this was built

Each project was developed with Claude as a pair programmer: describe the goal,
review the generated code, run the tests, then ask "why" until every line makes sense.

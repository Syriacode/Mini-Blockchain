# Mini-Blockchain



| # | Project | Concepts | Status |
|---|---------|----------|--------|
| 01 | [Simple chain](01-simple-chain) | Blocks, SHA-256, proof-of-work, validation, balances | ✅ |
| 02 | [Mintable stablecoin](02-stablecoin/GUIDE.md) | Upgradeable proxy, roles, minter allowances, pause, blocklist, fuzz & invariant tests | 🚧 |

## Run a project

```bash
cd 01-simple-chain
pip install pytest
python demo.py
python -m pytest -v
```


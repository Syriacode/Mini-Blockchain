# Mini-Blockchain



| # | Project | Concepts | Status |
|---|---------|----------|--------|
| 01 | [Simple chain](01-simple-chain) | Blocks, SHA-256, proof-of-work, validation, balances | ✅ |
| 02 | [Upgradeable stablecoin](https://github.com/Syriacode/upgradeable-stablecoin) *(own repo)* | Upgradeable proxy, roles, minter allowances, pause, blocklist, fuzz & invariant tests | ✅ |

## Run a project

```bash
cd 01-simple-chain
pip install pytest
python demo.py
python -m pytest -v
```


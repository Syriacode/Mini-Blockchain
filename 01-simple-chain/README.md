# 01 — Simple Chain

A minimal blockchain in ~100 lines of Python, no dependencies.

## What you learn

- **Blocks & hashing** — every block stores the SHA-256 hash of its contents and the previous block's hash.
- **Proof-of-work** — mining searches for a `nonce` that makes the hash start with N zeros.
- **Immutability** — change one old transaction and `is_valid()` fails; re-mining one block doesn't help because the next block still points to the old hash.
- **Account balances** — computed by replaying every transaction; the pending pool is counted to stop double-spends.

## Try it

```bash
python demo.py          # mine blocks, check balances, then tamper with history
python -m pytest -v     # 7 tests
```

## Exercises

1. Raise `difficulty` in `demo.py` from 4 to 5 and 6. How does mining time scale?
2. Write a test showing that an attacker who re-mines **every** block after the tampered one *does* get a valid chain. Why does a real network still reject it? (Hint: Project 04.)
3. Anyone can call `add_transaction("alice", ...)`. What's missing? (Answer: Project 02.)

## Known simplifications

No signatures, no networking, no difficulty adjustment, floats for amounts. Each is fixed in a later project.

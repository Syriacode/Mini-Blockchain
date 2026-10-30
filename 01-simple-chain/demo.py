"""Walk through the chain step by step:  python demo.py"""
import time

from blockchain import Blockchain

chain = Blockchain(difficulty=4)

print("Mining block 1 (reward to alice)...")
start = time.time()
b = chain.mine_pending("alice")
print(f"  nonce={b.nonce}  hash={b.hash[:20]}...  took {time.time() - start:.2f}s")

chain.add_transaction("alice", "bob", 3)
print("Mining block 2 (alice -> bob: 3, reward to bob)...")
b = chain.mine_pending("bob")
print(f"  nonce={b.nonce}  hash={b.hash[:20]}...")

print(f"\nBalances: alice={chain.balance_of('alice')}  bob={chain.balance_of('bob')}")
print(f"Chain valid? {chain.is_valid()}")

print("\nTampering: changing alice's payment to bob from 3 to 300...")
chain.chain[2].transactions[0]["amount"] = 300
print(f"Chain valid? {chain.is_valid()}")

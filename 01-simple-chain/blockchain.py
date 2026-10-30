"""A minimal blockchain: blocks, SHA-256 hashing, proof-of-work, and validation.

Project 01 of "Blockchain with Claude" — a step-by-step learning series.
"""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import asdict, dataclass

MINING_REWARD = 10
NETWORK = "NETWORK"  # sender name used for mining-reward transactions


@dataclass
class Block:
    index: int
    timestamp: float
    transactions: list
    previous_hash: str
    nonce: int = 0
    hash: str = ""

    def compute_hash(self) -> str:
        """Hash every field except the hash itself, in a deterministic order."""
        payload = {k: v for k, v in asdict(self).items() if k != "hash"}
        encoded = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()


class Blockchain:
    def __init__(self, difficulty: int = 3) -> None:
        self.difficulty = difficulty
        self.pending: list[dict] = []
        self.chain: list[Block] = [self._mine(Block(0, 0.0, [], "0" * 64))]

    # --- mining -----------------------------------------------------------
    def _mine(self, block: Block) -> Block:
        """Proof-of-work: find a nonce so the hash starts with `difficulty` zeros."""
        target = "0" * self.difficulty
        block.nonce = 0
        block.hash = block.compute_hash()
        while not block.hash.startswith(target):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    # --- transactions -----------------------------------------------------
    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """Queue a transaction; returns the index of the block that will hold it."""
        if amount <= 0:
            raise ValueError("amount must be positive")
        if sender != NETWORK and self.balance_of(sender) < amount:
            raise ValueError(f"{sender} has insufficient funds")
        self.pending.append({"sender": sender, "recipient": recipient, "amount": amount})
        return self.last_block.index + 1

    def mine_pending(self, miner: str) -> Block:
        """Bundle pending transactions plus a reward for the miner into a new block."""
        txs = self.pending + [{"sender": NETWORK, "recipient": miner, "amount": MINING_REWARD}]
        block = Block(
            index=self.last_block.index + 1,
            timestamp=time.time(),
            transactions=txs,
            previous_hash=self.last_block.hash,
        )
        self.chain.append(self._mine(block))
        self.pending = []
        return block

    def balance_of(self, address: str) -> float:
        """Confirmed balance minus anything already committed in the pending pool."""
        balance = 0.0
        for block in self.chain:
            for tx in block.transactions:
                if tx["recipient"] == address:
                    balance += tx["amount"]
                if tx["sender"] == address:
                    balance -= tx["amount"]
        for tx in self.pending:
            if tx["sender"] == address:
                balance -= tx["amount"]
        return balance

    # --- validation -------------------------------------------------------
    def is_valid(self) -> bool:
        target = "0" * self.difficulty
        for i, block in enumerate(self.chain):
            if block.hash != block.compute_hash():
                return False  # contents were changed after mining
            if not block.hash.startswith(target):
                return False  # proof-of-work missing
            if i > 0 and block.previous_hash != self.chain[i - 1].hash:
                return False  # link to the previous block is broken
        return True

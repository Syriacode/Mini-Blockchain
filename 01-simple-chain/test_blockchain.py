"""Tests for Project 01. Run with:  python -m pytest -v"""
import pytest

from blockchain import MINING_REWARD, Blockchain


@pytest.fixture
def chain():
    return Blockchain(difficulty=2)  # low difficulty keeps tests fast


def test_genesis_block_is_mined(chain):
    genesis = chain.chain[0]
    assert genesis.index == 0
    assert genesis.hash.startswith("00")
    assert chain.is_valid()


def test_mining_rewards_the_miner(chain):
    chain.mine_pending("alice")
    assert chain.balance_of("alice") == MINING_REWARD


def test_transfer_moves_funds(chain):
    chain.mine_pending("alice")
    chain.add_transaction("alice", "bob", 4)
    chain.mine_pending("carol")
    assert chain.balance_of("alice") == MINING_REWARD - 4
    assert chain.balance_of("bob") == 4


def test_cannot_overspend(chain):
    with pytest.raises(ValueError):
        chain.add_transaction("bob", "alice", 1)


def test_cannot_double_spend_in_pending_pool(chain):
    chain.mine_pending("alice")
    chain.add_transaction("alice", "bob", MINING_REWARD)
    with pytest.raises(ValueError):
        chain.add_transaction("alice", "carol", 1)


def test_tampering_breaks_validity(chain):
    chain.mine_pending("alice")
    chain.add_transaction("alice", "bob", 5)
    chain.mine_pending("alice")
    chain.chain[2].transactions[0]["amount"] = 500  # rewrite history
    assert not chain.is_valid()


def test_rehashing_one_block_still_breaks_the_link(chain):
    chain.mine_pending("alice")
    chain.mine_pending("alice")
    tampered = chain.chain[1]
    tampered.transactions[0]["amount"] = 999
    chain._mine(tampered)  # attacker redoes proof-of-work for this block only
    assert not chain.is_valid()  # block 2 still points to the old hash

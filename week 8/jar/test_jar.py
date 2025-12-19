import pytest
from jar import Jar

# -----------------------------
# Test init
# -----------------------------
def test_init():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0

def test_init_custom_capacity():
    j = Jar(20)
    assert j.capacity == 20

def test_init_negative_capacity():
    with pytest.raises(ValueError):
        Jar(-5)

# -----------------------------
# Test str
# -----------------------------
def test_str():
    j = Jar()
    assert str(j) == ""

def test_str_after_deposit():
    j = Jar()
    j.deposit(3)
    assert str(j) == "🍪🍪🍪"

# -----------------------------
# Test deposit
# -----------------------------
def test_deposit():
    j = Jar(10)
    j.deposit(4)
    assert j.size == 4

def test_deposit_multiple_times():
    j = Jar(10)
    j.deposit(3)
    j.deposit(2)
    assert j.size == 5

def test_deposit_overflow():
    j = Jar(5)
    with pytest.raises(ValueError):
        j.deposit(10)

def test_deposit_exact_capacity():
    j = Jar(5)
    j.deposit(5)
    assert j.size == 5

# -----------------------------
# Test withdraw
# -----------------------------
def test_withdraw():
    j = Jar(10)
    j.deposit(5)
    j.withdraw(2)
    assert j.size == 3

def test_withdraw_to_zero():
    j = Jar(10)
    j.deposit(3)
    j.withdraw(3)
    assert j.size == 0

def test_withdraw_more_than_size():
    j = Jar(10)
    j.deposit(3)
    with pytest.raises(ValueError):
        j.withdraw(5)

def test_withdraw_empty_jar():
    j = Jar()
    with pytest.raises(ValueError):
        j.withdraw(1)

# -----------------------------
# Test repr (optional)
# -----------------------------
def test_repr():
    j = Jar(10)
    assert repr(j) == "Jar(capacity=10, size=0)"
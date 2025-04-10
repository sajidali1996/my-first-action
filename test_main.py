import pytest
from main import is_prime, find_nth_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-5) == False

def test_find_nth_prime():
    assert find_nth_prime(1) == 2
    assert find_nth_prime(2) == 3
    assert find_nth_prime(3) == 5
    assert find_nth_prime(4) == 7
    assert find_nth_prime(10) == 29

def test_find_nth_prime_invalid_input():
    with pytest.raises(ValueError):
        find_nth_prime(0)
    with pytest.raises(ValueError):
        find_nth_prime(-1)
import is_odd
import pytest

def test_is_odd_3():
    assert is_odd.is_odd(3) == True

def test_is_odd_10():
    assert is_odd.is_odd(10) == False

def test_is_odd_3_2():
    with pytest.raises(Exception):
        assert is_odd.is_odd(3.2)

def test_is_odd_a():
    with pytest.raises(Exception):
        assert is_odd.is_odd('a')

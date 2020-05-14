import is_even
import pytest

def test_is_even_3():
    assert is_even.is_even(3) == False

def test_is_even_10():
    assert is_even.is_even(10) == True

def test_is_even_3_2():
    with pytest.raises(Exception):
        assert is_even.is_even(3.2)

def test_is_even_a():
    with pytest.raises(Exception):
        assert is_even.is_even('a')

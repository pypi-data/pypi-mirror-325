import pytest
from cellukeyga import add_two_digits

def test_add_two_digits_valid():
    assert add_two_digits(2, 4) == 6
    assert add_two_digits(0, 9) == 9
    assert add_two_digits(5, 5) == 10

def test_add_two_digits_invalid():
    with pytest.raises(ValueError):
        add_two_digits(-1, 50)
    with pytest.raises(ValueError):
        add_two_digits(100, 50)
    with pytest.raises(ValueError):
        add_two_digits(50, -1)
    with pytest.raises(ValueError):
        add_two_digits(50, 100)
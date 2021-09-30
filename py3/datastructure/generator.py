"""List comprehensions and generator expressions."""
import pytest


def test_type():
    a = [1, 2, 3]
    b = [chr(i) for i in a]
    c = (chr(i) for i in a)
    assert type(b) == list
    assert str(type(c)) == "<class 'generator'>"

if __name__ == "__main__":
    prefix = __file__ + '::'
    func = 'test_type'
    pytest.main([prefix + func, '-s'])

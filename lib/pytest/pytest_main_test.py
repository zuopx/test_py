""""""
import pytest


def test_collect():
    print("test_collect")
    pass


def test_collect1():
    pass


if __name__ == "__main__":
    pytest.main(["-v", "-s", f"{__file__}::{test_collect.__name__}"])

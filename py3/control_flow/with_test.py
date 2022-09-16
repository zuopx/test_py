""""""
import types
import contextlib

import pytest


class A:
    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass


class B:
    pass


@contextlib.contextmanager
def func1():
    yield "123"


@contextlib.contextmanager
def func2():
    return "123"


class TestWith:
    def test_type(self):
        with A():
            pass
        with func1():
            pass
        
        assert isinstance(func1, types.FunctionType)

    def test_exception(self):
        with pytest.raises(AttributeError):
            with B():
                pass
        with pytest.raises(TypeError):
            with func2():
                pass


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

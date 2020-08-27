'''什么情况下，python compiler 把函数内变量当作本地变量，或全局变量。'''
import pytest


def f1(a):
    print(a)
    print(b)


def f2(a):
    print(a)
    print(b)
    b = 9


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


def test_NameError():
    with pytest.raises(NameError):
        f1(3)


def test_UnboundLocalError():
    with pytest.raises(UnboundLocalError):
        f2(3)


b = 3


def test_global():
    f3(3)
    assert b == 9


if __name__ == "__main__":

    prefix = __file__ + '::'
    # pytest.main([prefix, '-s'])
    # pytest.main([prefix + 'test_NameError', '-s'])
    # pytest.main([prefix + 'test_UnboundLocalError', '-s'])
    pytest.main([prefix + 'test_global', '-s'])

'''
Learn protocol of context manager.

Context manager protocol:
-   __enter__()
-   __exit__()

with(... as) block:
with后面的语句生成context manager object;
context manager object执行__enter__()后返回的值赋给as后的变量；
'''
import pytest
import contextlib
import sys

class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, trackback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


@contextlib.contextmanager
def looking_glass2():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write = reverse_write

    yield 'JABBERWOCKY'

    sys.stdout.write = original_write


@contextlib.contextmanager
def looking_glass3():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write = reverse_write

    msg = ''
    try:
        yield 'JABBERWOCKY'      # __exit__ 从这一行后开始，故能捕获异常
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


def test_looking_glass1():
    with LookingGlass() as what:
        assert what == 'JABBERWOCKY'
        print(what)  # 预期输出'YKCOWREBBAJ'
        print('Percy Cho')  # 预期输出'ohC ycreP'
        a = 1 / 0  # 预期输出'Please DO NOT divide by zero!'
    print(what)  # 预期输出'JABBERWOCKY'
    print('Percy Cho')  # 预期输出'Percy Cho'

    with pytest.raises(NameError):
        with LookingGlass() as what:
            print(who)


def test_looking_glass2():
    with pytest.raises(ZeroDivisionError):
        with looking_glass2() as what:
            a = 1 / 0


def test_looking_glass3():
    with looking_glass3() as what:
        assert what == 'JABBERWOCKY'
        print(what)  # 预期输出'YKCOWREBBAJ'
        print('Percy Cho')  # 预期输出'ohC ycreP'
        a = 1 / 0  # 预期输出'Please DO NOT divide by zero!'
    print(what)  # 预期输出'JABBERWOCKY'
    print('Percy Cho')  # 预期输出'Percy Cho'


if __name__ == "__main__":
    prefix = __file__ + '::'
    func = 'test_looking_glass3'
    pytest.main([prefix + func, '-s'])

import functools
from inspect import getgeneratorstate
import pytest


def coroutine(func):
    @functools.wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager():
    count = 0
    result = 0
    while True:
        num = yield result
        result = ((result * count) + num) / (count + 1)
        count += 1


def test_averager():
    avg = averager()
    # next(avg)  # 使用了装饰器进行预操作，故不用这一句了。
    assert avg.send(1) == 1
    assert avg.send(2) == 1.5
    assert avg.send(3) == 2
    assert avg.send(4) == 2.5
    assert getgeneratorstate(avg) == 'GEN_SUSPENDED'
    avg.close()
    assert getgeneratorstate(avg) == 'GEN_CLOSED'


if __name__ == '__main__':
    prefix = __file__ + '::'
    func = 'test_averager'
    pytest.main([prefix + func, '-s'])

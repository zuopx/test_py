'''
delegating generator: 打通subgenerator和caller之间的通信通道。

subgenerator

caller
'''
from inspect import getgeneratorstate
from collections import namedtuple
import pytest

Result = namedtuple('Result', 'count average')


def averager():  # subgenerator
    count = 0
    average = 0
    while True:
        term = yield
        if term is None:
            break
        average = (count * average + term) / (count + 1)
        count += 1
    return Result(count, average)


def grouper(results, key):  # delegating generator
    while True:
        results[key] = yield from averager()

def test_averager():
    avg = averager()
    next(avg)
    avg.send(1)
    avg.send(2)
    avg.send(3)
    result = avg.send(None)
    # assert result == Result(3, 2)

if __name__ == "__main__":
    prefix = __file__ + '::'
    func = 'test_averager'
    pytest.main([prefix + func, '-s'])


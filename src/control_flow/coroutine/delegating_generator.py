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
    with pytest.raises(StopIteration):
        avg.send(None)


data = {
    'girls;kg':
    [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
    [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
    [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
    [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


def test_delegating_generator():
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # 返回一个generator object
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    print(results)


if __name__ == "__main__":
    prefix = __file__ + '::'
    func = 'test_delegating_generator'
    # func = 'test_averager'
    pytest.main([prefix + func, '-s'])

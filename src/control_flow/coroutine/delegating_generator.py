'''
delegating generator: 打通subgenerator和caller之间的通信通道。

subgenerator

caller

执行权的转移：
当gen调用yield from subgen，执行权转移到caller和subgen，只有当subgen终止了，执行权才回到gen。
'''
import sys
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
    return Result(count, average)  # Python2 doesn't support return with generators.


def grouper(results, key):  # delegating generator function
    while True:
        # 当subgen终止时，执行权才返回gen，results[key]的值为StopIteration.value。
        # 执行权返回到gen后，必须执行到yield，否则会出触发StopIteration异常。
        results[key] = yield from averager()


def grouper1(results, key):
    while True:
        avg = iter(averager())
        try:
            y = next(avg)  # prime generator
        except StopIteration as e:
            r = e.value
        else:
            while True:
                s = yield y
                try:
                    y = avg.send(s)
                except StopIteration as e:
                    r = e.value
                    break
        results[key] = r


def grouper2(results, key):
    while True:
        avg = iter(averager())
        try:
            y = next(avg)
        except StopIteration as e:
            r = e.value
        else:
            while True:
                try:
                    s = yield y
                except GeneratorExit as e:
                    try:
                        m = avg.close
                    except AttributeError:
                        pass
                    else:
                        m()
                    raise e
                except BaseException as e:
                    x = sys.exc_info()
                    try:
                        m = avg.throw
                    except AttributeError:
                        raise e
                    else:
                        try:
                            y = m(x)
                        except StopIteration as e:
                            r = e.value
                            break
                else:
                    try:
                        if s is None:
                            y = next(avg)
                        else:
                            y = avg.send(s)
                    except StopIteration as e:
                        r = e.value
                        break
        results[key] = r


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


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))


def test_delegating_generator():
    results = {}
    for key, values in data.items():
        group = grouper1(results, key)  # 返回一个delegating generator object
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    report(results)


if __name__ == "__main__":
    prefix = __file__ + '::'
    func = 'test_delegating_generator'
    pytest.main([prefix + func, '-s'])

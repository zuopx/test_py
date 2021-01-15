"""生成器。"""
import pytest
import itertools


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self._begin = begin
        self._step = step
        self._end = end

    def __iter__(self):
        result = type(self._begin + self._step)(self._begin)
        forever = self._end is None
        index = 0
        while forever or result < self._end:
            yield result
            index += 1
            result = self._begin + index * self._step


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + index * step


def aritprog_gen2(begin, step, end=None):
    first = type(begin + step)(begin)
    gen = itertools.count(first, step)
    if end is not None:
        gen = itertools.takewhile(lambda n: n < end, gen)
    return gen

class TestArithmeticProgression:
    def test_list(self):
        begin, step, end = 0, 1, 10
        # ap = ArithmeticProgression(0, 1, 10)
        ap = aritprog_gen2(begin, step, end)
        assert list(ap) == list(range(10))


if __name__ == "__main__":
    prefix = __file__ + '::'
    func = 'TestArithmeticProgression::test_list'
    pytest.main([prefix + func, '-s'])

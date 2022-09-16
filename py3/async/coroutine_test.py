"""协程

直接使用生成器实现协程，逻辑上可行，但语义上有点迷惑
>   引入async关键字，让函数变成异步函数，而又具有生成器的特性

yield from 则被 await 取代
"""
import types
import math
import collections

import pytest


def circle_area(r):
    return math.pi * r ** 2


async def circle_area_async(r):
    return math.pi * r ** 2


class TestCoroutine:
    def test_type(self):
        """类型

        协程对象不可迭代，但可等待，意味着可以用于await关键字之后
        """
        assert isinstance(circle_area, types.FunctionType)
        assert isinstance(circle_area(1), float)
        assert isinstance(circle_area_async, types.FunctionType)
        assert isinstance(circle_area_async(1), types.CoroutineType)

        assert not isinstance(circle_area_async(1), collections.abc.Iterable)

        assert hasattr(circle_area_async(1), "__await__")

    def test_stop_iteration(self):
        co = circle_area_async(1)

        with pytest.raises(StopIteration):
            while 1:
                co.send(None)

    def test_del(self):
        co = circle_area_async(1)
        with pytest.warns(RuntimeWarning):
            del co

    def test_await(self):
        """await job 等价于 yield from job._await__()"""
        class Job:
            def __await__(self):
                yield 1
                yield 2
                return 3

        async def do_job1(job):
            return await job

        def do_job2(job):
            return (yield from job.__await__())

        co1 = do_job1(Job())
        co2 = do_job2(Job())
        assert co1.send(None) == co2.send(None)
        assert co1.send(None) == co2.send(None)

        with pytest.raises(StopIteration):
            co1.send(None)
        with pytest.raises(StopIteration):
            co2.send(None)


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

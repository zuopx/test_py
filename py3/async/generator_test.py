"""生成器

生成器天生有记录任务上下文的特性，可用作协程的基本单元，但协程的使用还依赖任务调度。
"""
import sys
import types
import functools
import collections

import pytest


def iter_file_upper(path):
    with open(path) as f:
        for line in f:
            yield line.upper()


class TestGenerator:
    def test_type(self):
        """类型"""
        gen = iter_file_upper("README.md")
        assert isinstance(gen, types.GeneratorType)
        assert isinstance(gen, collections.abc.Iterable)
        assert isinstance(next, types.BuiltinFunctionType)

    def test_iter_file_upper(self):
        """使用"""
        for line in iter_file_upper("README.md"):
            print(line.strip())

    def test_StopIteration(self):
        """StopIteration"""
        gen = iter_file_upper("README.md")
        with pytest.raises(StopIteration):
            while 1:
                next(gen)

    def test_key_attr(self):
        """重要属性

        生成器持有一个静态帧，里面包含了状态、数据和程序
        """
        gen = iter_file_upper("README.md")
        assert hasattr(gen, "gi_frame")
        assert hasattr(gen, "gi_code")
        assert hasattr(gen, "gi_running")

    def test_code(self):
        """同一个code对象"""
        gen = iter_file_upper("README.md")
        assert gen.gi_code is gen.gi_frame.f_code
        assert gen.gi_code is iter_file_upper.__code__

    def test_frame(self):
        """静态帧的插入

        next -> gen_send_ex，将生成器的静态帧挂到当前调用链上
        yield，将生成器的帧栈从调用链揭开，并返回栈顶的值
        send，把值放到生成器帧栈的栈顶
        yield和send利用生成器栈顶来传值
        """

        def func():
            while 1:
                print(sys._getframe(0).f_code.co_name, sys._getframe(1).f_code.co_name)
                yield sys._getframe(0), sys._getframe(1)

        gen = func()
        frame0, frame1 = next(gen)
        assert frame0 is gen.gi_frame
        assert frame1 is sys._getframe(0)


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

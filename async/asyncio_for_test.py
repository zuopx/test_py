"""异步迭代器\生成器"""
import inspect
import typing
import asyncio

import pytest


def test_type():
    """def定义的本质上都是function，不同的function返回值类型不同"""
    def function():
        return 1

    def generator():
        yield 1

    async def async_function():
        return 1

    async def async_generator():
        yield 1

    assert inspect.isfunction(function)

    assert inspect.isgeneratorfunction(generator)

    assert inspect.iscoroutinefunction(async_function)

    assert inspect.isasyncgenfunction(async_generator)

    assert inspect.isgenerator(generator())
    assert inspect.iscoroutine(async_function())  # 协程，又名异步函数
    assert inspect.isasyncgen(async_generator())

    assert isinstance(generator(), typing.Iterable)  # 可迭代，用for
    assert isinstance(async_generator(), typing.AsyncIterable)  # 异步可迭代，用async for

    assert list(generator()), [1, ]

    with pytest.raises(TypeError, match="not iterable"):
        list(async_generator())


def test_async_for():
    print()

    async def async_generator():
        yield 1
        yield 2
        yield 3

    async def main():
        async for i in async_generator():
            print(i)

        print([i async for i in async_generator()])

    asyncio.run(main())


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

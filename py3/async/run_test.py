"""运行协程的三种机制
    asyncio.run
    await awaitable
    await task
"""
import asyncio

import pytest
import utils


class TestRun:
    @staticmethod
    def test_asyncio_run():
        """这里要注意，装饰器中要返回一个异步函数

        耗时2s
        """
        @utils.Decorator.print_start_end_async
        async def main():
            print("hello")
            await asyncio.sleep(2)
            print("world")

        asyncio.run(main())

    @staticmethod
    def test_await_awaitable():
        """两个coro依次执行，等同于yield

        耗时3s
        """
        @utils.Decorator.print_start_end_async
        async def say(delay, what):
            await asyncio.sleep(delay)
            print(what)

        async def main():
            await say(1, "hello")  # await，挂起main（调用方），直到协程返回
            await say(2, "world")

        asyncio.run(main())

    @staticmethod
    def test_await_same_coro():
        """await同一个协程

        RuntimeError: cannot reuse already awaited coroutine
        """
        @utils.Decorator.print_start_end_async
        async def say(delay, what):
            await asyncio.sleep(delay)
            print(what)

        async def main():
            coro = say(1, "hello")
            await coro

            with pytest.raises(RuntimeError):
                await coro

        asyncio.run(main())

    @staticmethod
    def test_await_task():
        """两个task会同时开始

        耗时2s
        """
        print()

        @utils.Decorator.print_start_end_async
        async def say(delay, what):
            await asyncio.sleep(delay)
            print(what)

        async def main():
            task1 = asyncio.create_task(say(1, "hello"))
            task2 = asyncio.create_task(say(2, "world"))

            await task1  # 阻塞main，不让main提前结束
            await task2

        asyncio.run(main())

    @staticmethod
    def test_send():
        """await task 等价于 coro.send(None)

        耗时2s
        """
        @utils.Decorator.print_start_end_async
        async def say(delay, what):
            await asyncio.sleep(delay)
            print(what)

        async def main():
            coro1 = say(1, "hello")
            coro2 = say(2, "world")

            try:
                coro1.send(None)
            except StopIteration:
                pass
            try:
                coro2.send(None)
            except StopIteration:
                pass

        asyncio.run(main())

    @staticmethod
    def test_run_until_complete():
        """两个Task会提前结束，因为事件循环已结束

        asyncio.run(main())，最终的都会跑到 loop.run_until_complete(main())
        loop的生命周期只由main()决定，
        当main()结束时，会调用_run_until_complete_cb，
        把loop._stopping设为true，同时跳出run_forever()中的while循环
        """
        @utils.Decorator.print_start_end_async
        async def say(delay, what):
            await asyncio.sleep(delay)
            print(what)

        async def main():
            task1 = asyncio.create_task(say(100, "hello"))
            task2 = asyncio.create_task(say(200, "world"))

            while True:
                await asyncio.sleep(3)

        asyncio.run(main())

    @staticmethod
    def test_task_list():
        """调度

        loop维护两个两个列表 ready 和 scheduled
        I/O阻塞，进入scheduled；可执行的，进行ready
        阻塞完成后，任务从scheduled转入ready，同时恢复调用栈 
        """
        print()

        async def say1(delay, what):
            await asyncio.sleep(delay)  # 进入阻塞，阻塞完成之后重新进入准备队列
            print(what)

        async def say2(delay, what):
            await say1(delay, what)

        async def main():
            await say1(100, "hello")

        asyncio.run(main())

    @staticmethod
    def test_return_await():
        """return await awaitable
        
        该语句会阻塞，直到awaitable执行到ruturn语句（而非yield）
        """
        print()

        async def say1(delay, what):
            await asyncio.sleep(delay)
            print(what)

        async def main():
            return await say1(100, "hello")

        asyncio.run(main())


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

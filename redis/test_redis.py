""""""
import asyncio

import redis
import redis.asyncio
import redis.asyncio


def func():
    r = redis.Redis(decode_responses=True)

    r.set("test", "1")

    value = r.get("test")

    print("test = ", value)


async def func_async():
    r = await redis.asyncio.Redis(decode_responses=True)

    await r.set("test_async", "1")

    value = await r.get("test_async")

    print("test_async = ", value)

    await r.aclose()  # 如果您在使用 Redis 的异步 API，确保在事件循环仍然处于活动状态时关闭连接。


async def func_async_with():
    async with redis.asyncio.from_url("redis://localhost", decode_responses=True) as r:
        await r.set("func_async_with", "1")

        value = await r.get("func_async_with")

        print("func_async_with = ", value)


def main():
    func()

    asyncio.run(func_async())
    asyncio.run(func_async_with())

    print("hello, world")


if __name__ == "__main__":
    main()

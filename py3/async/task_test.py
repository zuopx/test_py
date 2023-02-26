"""以协程的方式去运行，并得到返回值"""
import asyncio


async def func():
    ret = await add(1, 2)
    print(ret)


async def add(x, y):
    asyncio.create_task(_add(x, y))


async def _add(x, y):
    return x + y


def main():
    asyncio.run(func())
    print("hello, world")


if __name__ == "__main__":
    main()

"""脱离asyncio库，使用async和await。模拟事件循环，驱动协程对象。

python3.12 test_await.py
"""

from collections import deque


class MicroEventLoop:
    def __init__(self):
        self._tasks = deque()

    def add_task(self, coro):
        self._tasks.append(coro)

    def run(self):
        while self._tasks:
            task = self._tasks.popleft()
            try:
                result = task.send(None)
                print(f"任务暂停，状态值: {result}")
                self._tasks.append(task)
            except StopIteration as e:
                print(f"任务完成，返回值: {e.value}")


class SimpleAwaitable:
    def __init__(self, value):
        self.value = value

    def __await__(self):
        yield self.value  # 暂停点标识
        return "最终结果"


# 定义协程
async def task1():
    await SimpleAwaitable(1)
    await SimpleAwaitable(2)
    return "task1完成"


async def task2():
    await SimpleAwaitable("A")
    return "task2完成"

# 运行循环
loop = MicroEventLoop()
loop.add_task(task1())
loop.add_task(task2())
loop.run()

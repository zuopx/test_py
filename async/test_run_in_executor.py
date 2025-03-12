import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# 异步协程任务


async def async_task(task_id):
    print(f"[Async] 任务 {task_id} 开始 (线程: {threading.get_ident()})")
    await asyncio.sleep(1)  # 模拟异步I/O
    print(f"[Async] 任务 {task_id} 完成")

# 同步阻塞函数（模拟耗时操作）


def blocking_task(task_id):
    print(f"[Blocking] 任务 {task_id} 开始 (线程: {threading.get_ident()})")
    time.sleep(2)  # 模拟同步阻塞
    print(f"[Blocking] 任务 {task_id} 完成")
    return f"Result-{task_id}"

# 主异步函数


async def main():
    # 创建线程池（最大3线程）
    executor = ThreadPoolExecutor(max_workers=3)
    loop = asyncio.get_running_loop()

    # 同时运行异步任务和线程池任务
    async_results = []
    thread_results = []

    # 启动3个异步协程
    for i in range(3):
        async_results.append(async_task(i))

    # 启动5个阻塞任务到线程池
    for i in range(5):
        # 将阻塞任务提交到线程池
        future = loop.run_in_executor(executor, blocking_task, i)
        thread_results.append(future)

    # 等待所有任务完成
    await asyncio.gather(*async_results, *thread_results)

    # 输出线程任务结果
    print("\n线程任务结果:")
    for result in thread_results:
        print(await result)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"总耗时: {time.time() - start_time:.2f}秒")

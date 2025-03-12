import asyncio
import threading
import time
from concurrent.futures import Future

# 全局事件循环引用
loop = None


def event_loop_thread():
    """ 独立运行事件循环的线程 """
    global loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    print(f"事件循环线程启动（ID: {threading.get_ident()})")
    loop.run_forever()


async def async_task(name: str, delay: float) -> str:
    """ 模拟异步任务 """
    print(f"[{time.strftime('%H:%M:%S')}] 任务 {name} 开始（线程: {threading.get_ident()})")
    await asyncio.sleep(delay)
    return f"{name}-result"


def main_thread_operation():
    """ 主线程提交任务的示例 """
    # 提交协程到事件循环线程
    future = asyncio.run_coroutine_threadsafe(
        async_task("main-thread-task", 2),
        loop
    )

    # 阻塞等待结果（可选）
    try:
        result = future.result(timeout=5)
        print(f"[{time.strftime('%H:%M:%S')}] 主线程收到结果: {result}")
    except asyncio.TimeoutError:
        print("任务超时！")


def other_thread_operation():
    """ 其他线程提交任务的示例 """
    time.sleep(1)  # 模拟其他操作

    # 提交任务并获取 Future
    future = asyncio.run_coroutine_threadsafe(
        async_task("other-thread-task", 1),
        loop
    )

    # 非阻塞处理结果
    def callback(f: Future):
        try:
            print(f"[{time.strftime('%H:%M:%S')}] 其他线程收到结果: {f.result()}")
        except Exception as e:
            print(f"任务失败: {e}")

    future.add_done_callback(callback)
    print("非阻塞！！！")


if __name__ == "__main__":
    # 启动事件循环线程
    threading.Thread(target=event_loop_thread, daemon=True).start()

    # 等待事件循环初始化
    while loop is None:
        time.sleep(0.1)

    # 主线程操作
    main_thread_operation()

    # 启动其他工作线程
    threading.Thread(target=other_thread_operation).start()

    # 保持程序运行
    time.sleep(3)

    # 清理资源
    loop.call_soon_threadsafe(loop.stop)
    print("程序结束")

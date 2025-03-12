from concurrent.futures import ThreadPoolExecutor
import threading
import time
from queue import Queue


# 示例 1: 基础线程用法
def basic_thread_example():
    def worker(num):
        print(f"线程 {num} 开始执行")
        time.sleep(1)
        print(f"线程 {num} 结束执行")

    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# 示例 2: 使用锁保证线程安全
def locking_example():
    counter = 0
    lock = threading.Lock()

    def increment():
        nonlocal counter
        for _ in range(100000):
            with lock:
                counter += 1

    threads = []
    for _ in range(4):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"最终计数器值: {counter}")


# 示例 3: 使用队列实现生产者-消费者模式
def queue_example():
    q = Queue(maxsize=5)

    def producer():
        for i in range(10):
            item = f"产品 {i}"
            q.put(item)
            print(f"生产: {item}")
            time.sleep(0.1)

    def consumer():
        while True:
            item = q.get()
            if item is None:
                break
            print(f"消费: {item}")
            q.task_done()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    consumer_thread.start()
    producer_thread.start()

    producer_thread.join()
    q.put(None)  # 发送结束信号
    consumer_thread.join()


# 示例 4: 线程池实现
def thread_pool_example():
    def task(n):
        print(f"处理任务 {n}")
        time.sleep(0.5)
        return n * n

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(task, i) for i in range(5)]
        results = [f.result() for f in futures]

    print(f"所有任务结果: {results}")


if __name__ == "__main__":
    print("=== 基础线程示例 ===")
    basic_thread_example()

    print("\n=== 线程锁示例 ===")
    locking_example()

    print("\n=== 队列示例 ===")
    queue_example()

    print("\n=== 线程池示例 ===")
    thread_pool_example()

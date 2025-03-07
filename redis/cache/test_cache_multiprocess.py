import redis
import time
import multiprocessing


# 连接到 Redis 服务器
def create_redis_connection():
    return redis.Redis(host='localhost', port=6379, db=0)


def get_data(key):
    """
    从缓存中获取数据，如果没有则从数据源获取
    """
    r = create_redis_connection()

    # 尝试从缓存中获取数据
    cached_data = r.get(key)
    if cached_data:
        print(f"进程 {multiprocessing.current_process().name}: 从缓存中获取数据")
        return cached_data.decode('utf-8')
    else:
        print(f"进程 {multiprocessing.current_process().name}: 缓存未命中，获取数据中...")
        # 模拟从数据库或其他数据源获取数据
        data = fetch_data_from_source(key)

        # 将获取的数据存入缓存
        r.setex(key, 10, data)  # 设置缓存10秒过期
        return data


def fetch_data_from_source(key):
    # 模拟数据源延迟
    time.sleep(2)  # 假装这是一个耗时的操作
    return f"数据源返回的 {key}"


def worker(key):
    # 工作进程调用
    data = get_data(key)
    print(f"进程 {multiprocessing.current_process().name} 得到的数据: {data}")


if __name__ == "__main__":
    key = "example_key"

    # 创建多个进程
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=worker, args=(key,))
        processes.append(p)
        p.start()

    # 等待所有进程完成
    for p in processes:
        p.join()

import redis
import time

# 连接到 Redis 服务器
r = redis.Redis(host='localhost', port=6379, db=0)


def get_data(key):
    """
    从缓存中获取数据，如果没有则从数据源获取
    """
    # 尝试从缓存中获取数据
    cached_data = r.get(key)
    if cached_data:
        print("从缓存中获取数据")
        return cached_data.decode('utf-8')
    else:
        print("缓存未命中，获取数据中...")
        # 模拟从数据库或其他数据源获取数据
        data = fetch_data_from_source(key)

        # 将获取的数据存入缓存
        r.setex(key, 10, data)  # 设置缓存10秒过期
        return data


def fetch_data_from_source(key):
    # 模拟数据源延迟
    time.sleep(2)  # 假装这是一个耗时的操作
    return f"数据源返回的 {key}"


# 示例使用
if __name__ == "__main__":
    key = "example_key"

    # 第一次获取数据，应该会看到缓存未命中
    data = get_data(key)
    print(data)

    # 第二次获取相同的数据，应该会从缓存中获取
    data = get_data(key)
    print(data)

    # 等待缓存过期
    time.sleep(10)

    # 第三次获取数据，缓存已过期，需要重新获取
    data = get_data(key)
    print(data)

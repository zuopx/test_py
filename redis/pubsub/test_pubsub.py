import time
import argparse

import redis

# 连接到 Redis 服务器
REDIS_HOST = 'localhost'  # 替换为您的 Redis 服务器 IP 地址
REDIS_PORT = 6379         # Redis 服务器的端口


def publisher():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    while True:
        # 生成要发布的消息
        message = "缓存更新: 数据已更改"
        r.publish('cache_updates', message)
        print(f"发布消息: {message}")
        time.sleep(5)  # 每5秒发布一次消息


def subscriber():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    pubsub = r.pubsub()

    # 订阅频道
    pubsub.subscribe('cache_updates')

    print("订阅者已启动，等待消息...")

    for message in pubsub.listen():
        if message['type'] == 'message':
            # 收到消息时更新缓存
            print(f"收到消息: {message['data'].decode('utf-8')}")
            # 在这里可以实现更新本地缓存的逻辑


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pub", action="store_true", help="run publisher")
    parser.add_argument("--sub", action="store_true", help="run subscriber")
    args = parser.parse_args()

    if args.sub:
        subscriber()
    elif args.pub:
        publisher()
    else:
        parser.print_help()

import asyncio
import argparse

import redis.asyncio

# 连接到 Redis 服务器
REDIS_HOST = 'localhost'  # 替换为您的 Redis 服务器 IP 地址
REDIS_PORT = 6379         # Redis 服务器的端口


async def publisher():
    r = await redis.asyncio.Redis(host=REDIS_HOST, port=REDIS_PORT)
    try:
        while True:
            # 生成要发布的消息
            message = "缓存更新: 数据已更改"
            await r.publish('cache_updates', message)
            print(f"发布消息: {message}")
            await asyncio.sleep(5)  # 每5秒发布一次消息
    except asyncio.CancelledError:
        pass
    finally:
        await r.aclose()


async def subscriber():
    r = await redis.asyncio.Redis(host=REDIS_HOST, port=REDIS_PORT)
    pubsub = r.pubsub()

    # 订阅频道
    await pubsub.subscribe('cache_updates')

    print("订阅者已启动，等待消息...")

    try:
        async for message in pubsub.listen():
            if message['type'] == 'message':
                # 收到消息时更新缓存
                print(f"收到消息: {message['data'].decode('utf-8')}")
                # 在这里可以实现更新本地缓存的逻辑
    except asyncio.CancelledError:
        pass
    finally:
        await r.aclose()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pub", action="store_true", help="run publisher")
    parser.add_argument("--sub", action="store_true", help="run subscriber")
    args = parser.parse_args()

    if args.sub:
        asyncio.run(subscriber())
    elif args.pub:
        asyncio.run(publisher())
    else:
        parser.print_help()

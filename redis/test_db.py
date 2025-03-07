"""redis db

每个数据库都是独立的，您在一个数据库中存储的数据不会影响到其他数据库。
如果您使用 Python 来连接 Redis，可以在创建连接时选择数据库，或者在连接后使用 `SELECT` 命令。
"""
import redis


def main():
    r1 = redis.Redis(db=1)
    r2 = redis.Redis(db=2)

    r1.set("test_db", "1")
    print(r1.get("test_db"))

    print(r2.get("test_db"))
    r2.select(1)
    print(r2.get("test_db"))

    print("hello, world")


if __name__ == "__main__":
    main()

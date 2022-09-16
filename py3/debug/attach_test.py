# -*- coding: utf-8 -*-
"""debug一个运行的程序

1. 获取进程号
2. Attach using Process Id
"""
import os
import time


def func():
    print(os.getpid())

    tick = 0
    while True:
        print(tick)
        tick += 1

        time.sleep(5)


def main():
    func()
    print("hello, world")


if __name__ == "__main__":
    main()

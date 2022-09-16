""""""
import os
import sys
import psutil


class OS:
    @staticmethod
    def get_memory_usage():
        """当前进程的内存使用，单位MB"""
        return psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

class Runtime:
    @staticmethod
    def get_frame():
        return sys._getframe()
        


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

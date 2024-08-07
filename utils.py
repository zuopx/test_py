""""""
import os
import sys
import time
import psutil
import functools


class OS:
    @staticmethod
    def get_memory_usage():
        """当前进程的内存使用，单位MB"""
        return psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024


class Runtime:
    @staticmethod
    def get_frame():
        return sys._getframe()


class Decorator:
    @staticmethod
    def print_start_end_async(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            print(f"start at: {time.strftime('%X')}", )
            ret = await func(*args, **kwargs)
            print(f"ended at: {time.strftime('%X')}", )
            return ret
        return wrapper

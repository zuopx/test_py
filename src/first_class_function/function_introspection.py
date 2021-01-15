'''解构函数'''
import sys
import functools


class C:
    pass


def print_func_info(func):
    @functools.wraps(func)
    def _func(*args, **kwargs):
        print(func.__name__)
        print(args, kwargs)
        return func(*args, **kwargs)
    return _func


@print_func_info
def func(arg1: float = 0.0, arg2: float = 0.0):
    # print(sys._getframe().f_code.co_name)
    print(arg1 + arg2)


func(1, 2)

# print(func.__name__)
# print(func.__annotations__)
# print(func.__defaults__)
# print(func.__kwdefaults__)
# print(func.__globals__)

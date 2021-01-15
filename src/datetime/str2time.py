# coding=utf-8
import datetime
import time
import pytest


def test_str2datetime():
    start = datetime.datetime.now().replace(microsecond=0)
    dt = datetime.datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S')
    print dt

if __name__ == "__main__":
    prefix = __file__ + '::'
    pytest.main([prefix + 'test_str2datetime', '-s'])

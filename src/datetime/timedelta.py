# coding=utf-8
import datetime
import time
import pytest


def test_datetimedelta():
    start = datetime.datetime.now()
    time.sleep(1.5)
    end = datetime.datetime.now()
    end = end.replace(year=end.year + 1)

    print start
    print end 
    dur = end - start
    print type(dur)
    print dur

def test_total_second():
    start = datetime.datetime.now().replace(microsecond=0)
    end = datetime.datetime.now().replace(microsecond=0)
    end = end.replace(year=end.year + 1)

    dur = end - start
    print dur.total_seconds()

if __name__ == "__main__":
    prefix = __file__ + '::'
    pytest.main([prefix + 'test_total_second', '-s'])

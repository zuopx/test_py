'''
简单的协程示例，感性认识协程。

协程与函数：
主要区别在于调用方式，协程的执行不同于函数调用，反而类似CPU的中断。

协程与线程：
协程是单线程，协程的切换由程序自身控制，协程不需要锁机制。

协程与生成器：
协程是生成器，但是让协程有两个特点：
-   n = yield（中断）
-   send()方法（复活）
'''
from inspect import getgeneratorstate
import pytest

# 生产者消费者模式示例

import time


def consumer():
    r = ''
    while True:
        n = yield r  # 既返回值，也转让执行权
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'


def produce(c):
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 中断，并转让执行权给
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


def test_producer_consumer():
    c = consumer()
    produce(c)


# 使用协程实现运行中的平均数函数

def averager():
    count = 0
    result = 0
    while True:
        num = yield result
        result = ((result * count) + num) / (count + 1)
        count += 1


def test_averager():
    avg = averager()
    next(avg)
    assert avg.send(1) == 1
    assert avg.send(2) == 1.5
    assert avg.send(3) == 2
    assert avg.send(4) == 2.5
    assert getgeneratorstate(avg) == 'GEN_SUSPENDED'
    avg.close()
    assert getgeneratorstate(avg) == 'GEN_CLOSED'


if __name__ == '__main__':
    prefix = __file__ + '::'
    func = 'test_averager'
    pytest.main([prefix + func, '-s'])

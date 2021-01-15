'''closure is function and free variable'''
import pytest

def make_averager1():
    series = []

    def averager(value):
        series.append(value)
        return sum(series) / len(series)
    return averager


def make_averager2():
    count = 0
    total = 1

    def averager(value):
        count += 1
        total += value
        return total / count
    return averager


def make_averager3():
    count = 0
    total = 0.0

    def averager(value):
        nonlocal count, total
        count += 1
        total += value
        return total / count
    return averager

def test_closure():
    avg = make_averager1()
    print(avg.__closure__)

def test_UnboundLocalError():
    avg = make_averager2()
    with pytest.raises(UnboundLocalError):
        avg(1)

def test_nonlocal():
    avg = make_averager3()
    assert avg(1) == 1

if __name__ == "__main__":
    prefix = __file__
    pytest.main([prefix, '-s'])
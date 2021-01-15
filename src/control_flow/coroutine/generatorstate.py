'''
inspect.getgeneratorstate()
'''

from inspect import getgeneratorstate
import pytest


def test_generator_state():
    gen = (i for i in range(2))
    assert getgeneratorstate(gen) == 'GEN_CREATED'
    print(next(gen))
    assert getgeneratorstate(gen) == 'GEN_SUSPENDED'
    print(next(gen))
    with pytest.raises(StopIteration):
        next(gen)
    assert getgeneratorstate(gen) == 'GEN_CLOSED'


if __name__ == "__main__":
    prefix = __file__ + '::'
    func = 'test_generator_state'
    pytest.main([prefix + func, '-s'])

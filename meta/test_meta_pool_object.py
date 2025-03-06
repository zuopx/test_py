"""object pool

six.with_metaclass(MetaPoolObject)
"""
import six
import copy
import random


def _init(self, *args, **kwargs):
    return self


def _del(self):
    if len(self.__POOL__) < self.__POOL_LIMIT__:
        self.__POOL__.append(self)


def _gen_del(fn):
    def _del_fn(self):
        fn(self)
        if len(self.__POOL__) < self.__POOL_LIMIT__:
            self.__POOL__.append(self)

    return _del_fn


def ClearPool(cls):
    poolLimit, cls.__POOL_LIMIT__ = cls.__POOL_LIMIT__, 0
    cls.__POOL__ = []
    cls.__POOL_LIMIT__ = poolLimit


class MetaPoolObject(type):
    def __new__(mcs, name, bases, attr):
        attr['__POOL__'] = []
        if '__POOL_LIMIT__' not in attr:
            attr['__POOL_LIMIT__'] = 1000
        for base in bases:
            if isinstance(base, MetaPoolObject):
                break
        else:
            if '__del__' in attr:
                attr['__del__'] = _gen_del(attr['__del__'])
            else:
                attr['__del__'] = _del
            if 'init' not in attr:
                attr['init'] = _init
            attr['ClearPool'] = classmethod(ClearPool)
        return type.__new__(mcs, name, bases, attr)

    def __call__(cls, *args, **kwargs):
        if cls.__POOL__:
            return cls.__POOL__.pop().init(*args, **kwargs)
        obj = cls.__new__(cls)
        obj.__init__(*args, **kwargs)
        return obj


class RNGTracer(six.with_metaclass(MetaPoolObject, object)):
    __POOL_LIMIT__ = 10000

    DEBUG = 0
    PRINT_SEED = 1
    PRINT_OTHER = 2
    PRINT_ALL = PRINT_SEED | PRINT_OTHER

    def __init__(self, eid):
        self.eid = eid
        self.rng = random.Random()

    def __copy__(self):
        r = RNGTracer.__new__(RNGTracer)
        r.eid = self.eid
        r.rng = copy.copy(self.rng)

    def __getattr__(self, item):
        if self.DEBUG and (self.DEBUG & self.PRINT_SEED or item != "seed"):
            print(("entity:%s - rng use %s" % (self.eid, item)))
        return getattr(self.rng, item)


def main():
    rng = RNGTracer(1)
    print("hello, world")


if __name__ == "__main__":
    main()

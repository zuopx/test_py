"""通过实现二维向量熟悉特殊方法。"""
import math
import pytest


class Vector2d:

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)


class TestVector2d:
    def test_read_only_property(self):
        v = Vector2d(3, 4)
        with pytest.raises(AttributeError):
            v.x = 4

    def test_repr(self):
        v = Vector2d(3, 4)
        assert eval(repr(v)) == v

    def test_unpack(self):
        v = Vector2d(3, 4)
        x, y = v
        assert (x, y) == (3, 4)


if __name__ == "__main__":
    pytest.main([__file__, '-s'])

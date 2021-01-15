'''python3 private attributes.'''
import pytest

data = {
    'id': 1,
    'name': 'foo'
}


class C:
    def __init__(self):
        self.__data = dict(data)


if __name__ == "__main__":
    c = C()

    with pytest.raises(AttributeError):
        print(c.__data)

    assert c._C__data == data

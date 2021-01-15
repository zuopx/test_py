'''
Actual construtor: __new__(): it's a class method, and it must return an instance as the first argument of __init__.
'''

from collections import abc
import keyword


class FrozenJSON:
    """A read-only façade for navigating a JSON-like object
       using attribute notation
    """

    def __new__(cls, arg):  # <1>
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)  # <2>
        elif isinstance(arg, abc.MutableSequence):  # <3>
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])  # <4>


if __name__ == "__main__":
    player1 = {
        'pid': 1,
        'name': 'foo',
        'role': [
            {
                'rid': 0,
                'group': 0,
            },
            {
                'rid': 1,
                'group': 1,
            }
        ]
    }
    player2 = 'foo'

    da_player = FrozenJSON(player2)

    roles = da_player.role

    print(da_player.__data)

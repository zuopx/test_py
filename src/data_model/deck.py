import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:
    """仅仅通过实现两个特殊方法，使Deck对象表现得像python内置类型。"""
    RANKS = [str(n) for n in range(2, 11)] + list('JQKA')
    SUITS = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for rank in self.RANKS for suit in self.SUITS]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
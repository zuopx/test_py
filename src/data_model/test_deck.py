import pytest
from deck import Card, Deck


@pytest.fixture()
def d():
    return Deck()


class TestDeck:

    def test_len(self, d):
        assert len(d) == 52

    def test_getitem(self, d):
        assert d[0] == Card('2', 'spades')

    def test_random_pick(self, d):
        import random
        assert isinstance(random.choice(d), Card)

    def test_slicing(self, d):
        assert len(d[:10]) == 10
        assert len(d[12::13]) == 4

    def test_reversed(self, d):
        assert next(reversed(d)) == Card('A', 'hearts')


if __name__ == "__main__":
    prefix = __file__ + '::TestDeck::'
    pytest.main([prefix + 'test_reversed', '-s'])

""""""
import collections


class TestCounter:
    def setup_method(self):
        self.counter = collections.Counter()

    def test_dict(self):
        self.counter["a"] = 1
        self.counter["b"] += 2
        assert self.counter.most_common(1) == [("b", 2)]


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

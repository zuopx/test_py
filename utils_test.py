""""""
import utils


class TestOS:
    def test_get_memory_usage(self):
        print(utils.OS.get_memory_usage())


def main():
    TestOS().test_get_memory_usage()

    print("hello, world")


if __name__ == "__main__":
    main()

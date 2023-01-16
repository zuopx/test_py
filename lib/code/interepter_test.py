""""""
from code import InteractiveInterpreter


inpt = InteractiveInterpreter()


class TestInterpreter:

    @staticmethod
    def test_print():
        """会输出"""
        src = "print('hello, world')"
        more = inpt.runsource(src)

    @staticmethod
    def test_ret():
        """会输出"""
        src = "import os"
        inpt.runsource(src)
        src = "os.getcwd()"
        inpt.runsource(src)

    @staticmethod
    def test_locals():
        src = "import os"
        inpt.runsource(src)
        src = "cwd = os.getcwd()"
        inpt.runsource(src)

        assert "os" in inpt.locals
        assert "cwd" in inpt.locals


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

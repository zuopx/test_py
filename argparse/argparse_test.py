"""argparse参数解析

两种参数：位置参数和可选参数
多种action，action决定了会怎么灵活解析参数
"""
import argparse

import pytest


class TestArgparse:
    def test_position_args(self):
        """parse_args的返回值类型未Namespace，并非dict，但可取其__dict__"""
        parser = argparse.ArgumentParser()
        parser.add_argument("src")

        with pytest.raises(SystemExit):
            parser.parse_args([])

        args = parser.parse_args(["trunk"])
        with pytest.raises(TypeError):
            src = args["src"]

        src = args.src
        assert src == "trunk"

    def test_keyword_args(self):
        parser = argparse.ArgumentParser(conflict_handler="resolve")
        parser.add_argument("-s", "--src")

        parser.print_help()

        assert parser.parse_args([]).src is None

        assert parser.parse_args(["-s", "trunk"]).src == "trunk"
        assert parser.parse_args(["--src", "trunk"]).src == "trunk"

        parser.add_argument("--src", required=True)
        with pytest.raises(SystemExit):
            parser.parse_args([])

    def test_action(self):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    print(args.echo)


if __name__ == "__main__":
    main()

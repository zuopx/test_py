"""字节码之code对象

https://www.imooc.com/read/76/article/1915
"""
import inspect
import dis

import pytest


@pytest.fixture
def code():
    with open(r"py3\bytecode\demo.py") as f:
        text = f.read()

    return compile(text, "demo.py", "exec")


class TestCode:
    @staticmethod
    def test_type(code):
        assert inspect.iscode(code)

    @staticmethod
    def test_co_names(code):
        """名字列表"""
        assert hasattr(code, "co_names")  # 名字列表
        assert isinstance(code.co_names, tuple)
        assert "PI" in code.co_names and "Dog" in code.co_names
        print(code.co_names)

    @staticmethod
    def test_co_consts(code):
        """常量列表，里面会嵌套一些code对象

        每个作用域对应着一个代码对象，子作用域代码对象位于父作用域代码对象的常量列表里
        """
        assert hasattr(code, "co_consts")
        assert isinstance(code.co_consts, tuple)
        assert inspect.iscode(code.co_consts[3])
        print(code.co_consts)
        print(code.co_consts[3].co_consts)

    @staticmethod
    def test_opcode(code):
        """反编译opcode"""
        assert hasattr(code, "co_code")
        assert isinstance(code.co_code, bytes)

        print()
        print(dis.dis(code))


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

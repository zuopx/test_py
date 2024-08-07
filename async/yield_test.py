"""yield/yield from背后的字节码"""
import inspect
import dis


def co_process():
    yield 1
    yield 2


def co_process2():
    yield from co_process()
    return 3


async def co_process3():
    return 3


def use_co_process():
    co = co_process()
    co.send(None)


def use_co_process2():
    co = co_process2()
    co.send(None)


class TestYield:
    @staticmethod
    def test_type():
        gen1 = co_process()
        gen2 = co_process2()
        assert inspect.isgenerator(gen1)
        assert inspect.isgenerator(gen2)

    @staticmethod
    def test_co_flags():
        assert co_process.__code__.co_flags & 0x20
        assert co_process2.__code__.co_flags & 0x20

    @staticmethod
    def test_opcode():
        print()
        print(dis.dis(co_process.__code__))
        print(dis.dis(co_process2.__code__))
        print(dis.dis(use_co_process.__code__))
        print(dis.dis(use_co_process2.__code__))


def test_yield_from_value():
    """yield from表达式的值是异常的值，所以必须要触发StopIteration异常

    yield from 不能用在async函数中
    """
    def co():
        yield 1
        return 2

    def co2():
        r = yield from co()
        print(r)

    c2 = co2()
    print(list(c2))


def main():
    test_yield_from_value()

    print("hello, world")


if __name__ == "__main__":
    main()

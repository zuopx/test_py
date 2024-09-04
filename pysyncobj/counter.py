"""pysyncobj

https://github.com/bakwc/PySyncObj?tab=readme-ov-file#usage

https://raft.github.io/
"""
import time

from pysyncobj import SyncObj, replicated


class MyCounter(SyncObj):
    def __init__(self):
        super(MyCounter, self).__init__('localhost:10000', ['localhost:10001', 'localhost:10002'])
        self.__counter = 0

    @replicated
    def incCounter(self):
        self.__counter += 1

    def getCounter(self):
        return self.__counter


def main():
    print("hello, world")

    counter = MyCounter()

    while True:
        counter.incCounter()
        print(counter.getCounter())

        time.sleep(1)


if __name__ == "__main__":
    main()

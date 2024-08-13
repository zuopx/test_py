"""python2 script"""
import sys
import lib2to3


def main():
    for p in sys.path:
        print p

    print "hello, world"


if __name__ == "__main__":
    main()

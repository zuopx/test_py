"""对异常编程"""
import sys
import traceback
import unittest


def divide():
    return 1 / 0


class TestException(unittest.TestCase):
    def testExcInfo(self):
        try:
            divide()
        except Exception as e:
            print(e)
            print(str(e))
            print(repr(e))

            exc_type, exc_value, exc_trace = sys.exc_info()
            self.assertEqual(e, exc_value)
            print(exc_type)
            print(exc_value)
            print(repr(exc_trace))
            traceback.print_exc()

    def testTraceback(self):
        try:
            divide()
        except Exception as e:
            traceback.print_exc()
            traceback.print_stack()


if __name__ == "__main__":
    unittest.main()

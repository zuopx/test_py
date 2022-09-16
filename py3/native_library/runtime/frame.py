"""探究调用栈的frame对象"""
import sys

def get_frame():
    frame0 = sys._getframe()
    print(frame0.f_code.co_name)
    frame1 = sys._getframe(1)
    print(frame1.f_code.co_name)

    print("Done!")

class A:
    get_frame()

if __name__ == "__main__":
    pass
"""
'?' Represents one to three characters
"""

import re


def helper1():
    # str1 = input()
    # str2 = input()
    str1 = 'abcdefg'
    str2 = 'a?c'
    print(str1, str2)
    str2 = str2.replace('?', r'[^\0]{1,3}')
    print(str2)

    b = re.match(str2, str1)
    print(b)



if __name__ == "__main__":
    helper1()

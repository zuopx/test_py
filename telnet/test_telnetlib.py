"""telnetlib

>>> import telnetlib
<stdin>:1: DeprecationWarning: 'telnetlib' is deprecated and slated for removal in Python 3.13

>>> from telnetlib import Telnet
>>> tn = Telnet('www.python.org', 79)   # connect to finger port
>>> tn.write(b'guido\r\n')
>>> print(tn.read_all())
Login       Name               TTY         Idle    When    Where
guido    Guido van Rossum      pts/2        <Dec  2 11:10> snag.cnri.reston..
"""


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

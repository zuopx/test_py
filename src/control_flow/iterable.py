# coding=utf-8
"""
可迭代对象，必须实现__iter__方法，并且返回一个迭代器；
迭代器，本身是一个可迭代对象，而且实现__next__方法。
"""
import re
import reprlib


class Sentence:
    RE_WORD = re.compile('\w+')

    def __init__(self, text):
        self.text = text
        self.words = self.RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self):
        pass

    def __next__(self):
        pass

    def __iter__(self):
        return self

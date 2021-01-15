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
        """此处返回一个迭代器，而不是返回本身。这样每次调用iter都返回一个新的迭代器。"""
        pass


class SentenceIterator:
    def __init__(self, words):
        self.ind = 0
        self.words = words

    def __next__(self):
        try:
            word = self.words[self.ind]
        except IndexError:
            raise StopIteration()
        self.ind += 1
        return word

    def __iter__(self):
        return self


# 手动实现迭代器类(__next__)
class Sentence1(Sentence):

    def __iter__(self):
        return SentenceIterator(self.words)


# generetor function
class Sentence2(Sentence):
    def __iter__(self):
        for word in self.words:
            yield word


# lazy generator function
class Sentence3(Sentence):
    def __iter__(self):
        for match in self.RE_WORD.finditer(self.text):
            yield match.group()


# generator expression
class Sentence4(Sentence):
    def __iter__(self):
        return (match.group() for match in self.RE_WORD.finditer(self.text))

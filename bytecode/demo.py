PI = 3.14


def circle_area(r):
    return PI * r ** 2


class Dog(object):

    def __init__(self, name):
        self.name = name

    def yelp(self):
        print('woof, i am', self.name)

"""属性优先级"""


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        assert age > 0
        self._age = age

    def hello(self):
        return "hello" 


class TestAttrPriority:
    @staticmethod
    def test_priority():
        child = Child("Tom", 10)

        child.__dict__["age"] = 11
        child.__dict__["hello"] = lambda: "hi"

        assert child.age == 10
        assert child.hello() == "hi"


def main():
    print("hello, world")


if __name__ == "__main__":
    main()

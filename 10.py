import unittest


def fake_init(*args, **kwargs):
    pass


class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        else:
            cls.__init__ = fake_init
        return cls.instance


class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step


class GlobalCounter(Singleton, Counter):
    pass


class Tests(unittest.TestCase):
    def test(self):
        gc1 = GlobalCounter(30, 40)
        gc2 = GlobalCounter(20, 50)
        self.assertEqual(id(gc1), id(gc2))


unittest.main()

import unittest


def sum(x, y):
    return x + y


def specialize(func, *args, **kwargs):
    def part_fun(*add_args, **add_kwargs):
        return func(*args, *add_args, **kwargs, **add_kwargs)

    return part_fun


class Tests(unittest.TestCase):
    def test1(self):
        plus_one = specialize(sum, y=1)
        self.assertEqual(plus_one(10), 11)

    def test2(self):
        plus_one = specialize(sum, x=5)
        self.assertEqual(plus_one(y=20), 25)

    def test3(self):
        just_two = specialize(sum, 1, 1)
        self.assertEqual(just_two(), 2)


unittest.main()

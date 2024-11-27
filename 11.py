import unittest


def take(seq, n):
    res = []
    for i in range(n):
        res.append(next(seq))
    return res


def cycle(iterable):
    while True:
        yield from iterable


def chain(*iterables):
    for i in iterables:
        yield from i


class Tests(unittest.TestCase):
    def test_cycle(self):
        result = take(cycle([1, 2, 3]), 10)
        expected = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
        self.assertEqual(result, expected)

    def test_chain(self):
        result = list(chain([1, 2, 3], ['a', 'b'], [42, 13, 7]))
        expected = [1, 2, 3, 'a', 'b', 42, 13, 7]
        self.assertEqual(result, expected)


unittest.main()

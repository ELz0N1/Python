import unittest


def matrix(string):
    return [[int(elem) for elem in line.split()] for line in string.split("|")]


class Tests(unittest.TestCase):
    def test1(self):
        data = "1 2 3 | 4 5 6 | 7 8 9"
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9]], matrix(data))

    def test2(self):
        data = "  1  \t\n \r 2   3  \r\n|\t  \t4  \t\r\v 5   6 "
        self.assertEqual([[1, 2, 3], [4, 5, 6]], matrix(data))

    def test3(self):
        data = "1|2|3|4|5|6|7|8|9"
        self.assertEqual([[1], [2], [3], [4], [5], [6], [7], [8], [9]], matrix(data))


unittest.main()

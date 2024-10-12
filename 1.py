import unittest


def bits_count(number: int):
    count = 0

    if number >= 0:
        while number:
            count += number % 2
            number >>= 1
    else:
        number = abs(number)
        good_one = False
        while number:
            if number % 2:
                good_one = True
            elif good_one:
                count += 1
            number >>= 1
        count += 2

    return count


class Tests(unittest.TestCase):
    def test_positive(self):
        tests = [
            (0, 0),
            (4, 1),
            (7, 3),
            (10, 2),
            (127, 7),
            (2 ** 31 - 1, 31)
        ]

        for number, expected in tests:
            self.assertEqual(expected, bits_count(number))

    def test_negative(self):
        tests = [
            (-1, 2),
            (-4, 2),
            (-69, 6),
            (-123, 3),
            (-127, 2),
            (-2 ** 31, 2)
        ]

        for number, expected in tests:
            self.assertEqual(expected, bits_count(number))


unittest.main()

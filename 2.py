import unittest


def my_zip(list1, list2):
    result = []
    i = 0
    while i < len(list1) and i < len(list2):
        result.append((list1[i], list2[i]))
        i += 1
    return result


class Tests(unittest.TestCase):
    def test(self):
        tests = [
            ([1, 2, 3], ['a', 'b']),
            ([1, 2, 3], [4, 5, 6]),
            (['c', 2, 2.5], ['5', [], ()]),
            (['a', 4, "string", 9.0], [0]),
            ([], [])
        ]

        for list1, list2 in tests:
            self.assertEqual(my_zip(list1, list2), list(zip(list1, list2)))
            self.assertEqual(my_zip(list2, list1), list(zip(list2, list1)))


unittest.main()

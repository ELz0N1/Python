import unittest


def my_zip(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        result.append((list1[i], list2[i]))
    return result


def my_zip_using_generator(list1, list2):
    return [(list1[i], list2[i]) for i in range(min(len(list1), len(list2)))]


class Tests(unittest.TestCase):
    def test_my_zip(self):
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

    def test_my_zip_using_generator(self):
        tests = [
            ([1, 2, 3], ['a', 'b']),
            ([1, 2, 3], [4, 5, 6]),
            (['c', 2, 2.5], ['5', [], ()]),
            (['a', 4, "string", 9.0], [0]),
            ([], [])
        ]

        for list1, list2 in tests:
            self.assertEqual(my_zip_using_generator(list1, list2), list(zip(list1, list2)))
            self.assertEqual(my_zip_using_generator(list2, list1), list(zip(list2, list1)))


unittest.main()

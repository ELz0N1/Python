import unittest


def flatten(in_list):
    new_list = []
    for i in in_list:
        if isinstance(i, list):
            new_list += flatten(i)
        else:
            new_list.append(i)

    return new_list


def flatten_with_depth(in_list, depth=None):
    new_list = []
    for i in in_list:
        if isinstance(i, list) and (depth is None or depth > 0):
            new_list += flatten_with_depth(i, None if depth is None else depth - 1)
        else:
            new_list.append(i)

    return new_list


class Tests(unittest.TestCase):
    def test_flatten(self):
        tests = [
            ([1, 2, [4, 5], [6, [7]], 8], [1, 2, 4, 5, 6, 7, 8]),
            ([1, [2, [4, 5], 6, 7], 8], [1, 2, 4, 5, 6, 7, 8]),
            ([1, [2, [4, [5, [6, [7, [8]]]]]]], [1, 2, 4, 5, 6, 7, 8]),
            ([[1], [2], [4], [5], [6], [7], [8]], [1, 2, 4, 5, 6, 7, 8]),
            ([1, 2, 4, 5, 6, 7, 8], [1, 2, 4, 5, 6, 7, 8]),
        ]

        for array, expected in tests:
            self.assertEqual(flatten(array), expected)

    def test_flatten_with_depth(self):
        tests = [
            ([1, 2, [4, 5], [6, [7]], 8], 1, [1, 2, 4, 5, 6, [7], 8]),
            ([1, [2, [4, 5], 6, 7], 8], 2, [1, 2, 4, 5, 6, 7, 8]),
            ([1, [2, [4, [5, [6, [7, [8]]]]]]], 4, [1, 2, 4, 5, 6, [7, [8]]]),
            ([[1], [2], [4], [5], [6], [7], [8]], 1, [1, 2, 4, 5, 6, 7, 8]),
            ([1, 2, 4, 5, 6, 7, 8], 0, [1, 2, 4, 5, 6, 7, 8]),
        ]

        for array, depth, expected in tests:
            self.assertEqual(flatten_with_depth(array, depth), expected)

    def test_flatten_depth_without_param_depth(self):
        tests = [
            ([1, 2, [4, 5], [6, [7]], 8], [1, 2, 4, 5, 6, 7, 8]),
            ([1, [2, [4, 5], 6, 7], 8], [1, 2, 4, 5, 6, 7, 8]),
            ([1, [2, [4, [5, [6, [7, [8]]]]]]], [1, 2, 4, 5, 6, 7, 8]),
            ([[1], [2], [4], [5], [6], [7], [8]], [1, 2, 4, 5, 6, 7, 8]),
            ([1, 2, 4, 5, 6, 7, 8], [1, 2, 4, 5, 6, 7, 8]),
        ]

        for array, expected in tests:
            self.assertEqual(flatten_with_depth(array), expected)


unittest.main()

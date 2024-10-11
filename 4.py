import unittest


def reverse_dict(dict):
    result = {}

    for key, value in dict.items():
        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)

    for key, value in result.items():
        result[key] = value[0] if len(value) == 1 else tuple(value)

    return result


class Tests(unittest.TestCase):
    def test(self):
        d = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
        expected = {97832: ("Ivanov", "Kuznecov"), 55521: "Petrov"}
        self.assertEqual(expected, reverse_dict(d))

    def test_unhashable_vals(self):
        d = {'a': 1, 'b': [0, 2], (3): 1, 4: {3}, ('a', 'b'): 5}

        exception = False
        try:
            reverse_dict(d)
        except TypeError:
            exception = True

        self.assertTrue(exception)


unittest.main()

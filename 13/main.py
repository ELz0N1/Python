import foreign
import unittest


class Tests(unittest.TestCase):
    def test(self):
        matrix = [[1.0, 2.0], [3.0, 4.0]]
        result = foreign.foregin_matrix_power(matrix, 3)
        expected = [[37, 54], [81, 118]]
        self.assertEqual(result, expected)

    def test_identity_matrix(self):
        identity_matrix = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
        result = foreign.foregin_matrix_power(identity_matrix, 5)
        self.assertEqual(result, identity_matrix)

    def test_one_exponent(self):
        matrix = [[1.0, 2.0], [3.0, 4.0]]
        result = foreign.foregin_matrix_power(matrix, 1)
        self.assertEqual(result, matrix)

    def test_negative_exponent(self):
        with self.assertRaises(ValueError):
            foreign.foregin_matrix_power([[1.0, 2.0], [3.0, 4.0]], -1)

    def test_non_square_matrix(self):
        with self.assertRaises(ValueError):
            foreign.foregin_matrix_power([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], 2)


unittest.main()

import io
import unittest
import unittest.mock


def format_table(benchmarks, algos, results):
    first_column_len = max(map(len, benchmarks + ['Benchmark']))

    col_len = [max(map(len, [(algos[i])] + [(str(results[0][i]))] + [(str(results[1][i]))]))
               for i in range(len(algos))]

    header = f"| {'Benchmark': <{first_column_len}} |"
    total_len = first_column_len + len(algos) + 2  # +2 whitespaces

    for i in range(len(algos)):
        header += f" {algos[i]: <{col_len[i]}} |"
        total_len += col_len[i] + 2  # +2 whitespaces
        i += 1
    print(header)

    print(f"|{'-' * total_len}|")

    for i in range(len(benchmarks)):
        line = f"| {benchmarks[i]: <{first_column_len}} |"
        for j in range(len(results[i])):
            line += f" {results[i][j]: <{col_len[j]}} |"
        print(line)


class Tests(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test1(self, mock_stdout):
        format_table(["best case", "worst case"],
                     ["quick sort", "merge sort", "bubble sort"],
                     [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])

        expected_output = """| Benchmark  | quick sort | merge sort | bubble sort |
|----------------------------------------------------|
| best case  | 1.23       | 1.56       | 2.0         |
| worst case | 3.3        | 2.9        | 3.9         |
"""
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test2(self, mock_stdout):
        format_table(["best case", "average time", "worst case"],
                     ["quick sort", "merge sort"],
                     [[1.23, 1.56], [2.26, 2.23], [3.3, 2.9]])

        expected_output = """| Benchmark    | quick sort | merge sort |
|----------------------------------------|
| best case    | 1.23       | 1.56       |
| average time | 2.26       | 2.23       |
| worst case   | 3.3        | 2.9        |
"""
        self.assertEqual(mock_stdout.getvalue(), expected_output)


unittest.main()

import io
import functools
import unittest
import unittest.mock


def deprecated(func=None, since=None, will_be_removed=None):
    if func is None:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)

    message = (f"Warning: function {func.__name__} is deprecated{'' if since is None else f' since version {since}'}."
               f" It will be removed in {'future versions' if will_be_removed is None else f'version {will_be_removed}'}.")

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(message)
        return func(*args, **kwargs)

    return inner


@deprecated
def foo():
    print("Hello from foo\n")


@deprecated(since="1.0.3")
def bar():
    print("Hello from bar\n")


@deprecated(will_be_removed="2.0.1")
def buzz():
    print("Hello from buzz\n")


@deprecated(since="1.1.4", will_be_removed="1.2.0")
def fizz():
    print("Hello from fizz\n")


class Tests(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_foo(self, mock_stdout):
        foo()
        expected_output = ("Warning: function foo is deprecated. It will be removed in future versions.\n"
                           "Hello from foo\n\n")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bar(self, mock_stdout):
        bar()
        expected_output = (
            "Warning: function bar is deprecated since version 1.0.3. It will be removed in future versions.\n"
            "Hello from bar\n\n")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_buzz(self, mock_stdout):
        buzz()
        expected_output = ("Warning: function buzz is deprecated. It will be removed in version 2.0.1.\n"
                           "Hello from buzz\n\n")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_fizz(self, mock_stdout):
        fizz()
        expected_output = (
            "Warning: function fizz is deprecated since version 1.1.4. It will be removed in version 1.2.0.\n"
            "Hello from fizz\n\n")
        self.assertEqual(mock_stdout.getvalue(), expected_output)


unittest.main()

import unittest
import functools


def coroutine(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        g = f(*args, **kwargs)
        next(g)
        return g

    return wrapper


@coroutine
def storage():
    values = set()
    was_there = False
    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


class Tests(unittest.TestCase):
    def test(self):
        st = storage()
        self.assertFalse(st.send(42))
        self.assertTrue(st.send(42))


unittest.main()

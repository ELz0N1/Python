import unittest


class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = {}
        self.size = len(self.cache)
        self.call_order = []

    def get(self, key):
        if key in self.cache:
            self.call_order.remove(key)
            self.call_order.append(key)
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.call_order.remove(key)
            self.call_order.append(key)
        else:
            if self.size >= self.capacity:
                oldest_key = self.call_order.pop(0)
                del self.cache[oldest_key]
            self.cache[key] = value
            self.call_order.append(key)


class Tests(unittest.TestCase):
    def test(self):
        lrucache = LRUCache(2)
        lrucache.put(1, 1)
        lrucache.put(2, 2)
        self.assertEqual(lrucache.get(1), 1)
        lrucache.put(3, 3)
        self.assertEqual(lrucache.get(2), 2)
        lrucache.put(4, 4)
        self.assertEqual(lrucache.get(1), 1)
        self.assertEqual(lrucache.get(3), 3)
        self.assertEqual(lrucache.get(4), 4)


unittest.main()

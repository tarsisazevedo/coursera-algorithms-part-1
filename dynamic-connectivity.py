import unittest

class DynamicConectivity(object):
    def __init__(self, items):
        self.items = range(items)

    def union(self, p, q):
        item = self.items[p]
        for index, it in enumerate(self.items):
            if item == it:
                self.items[index] = self.items[q]

    def connected(self, p, q):
        return self.items[p] == self.items[q]


class DynamicConectivityTestCase(unittest.TestCase):
    def setUp(self):
        self.dc = DynamicConectivity(10)

    def test_should_init_with_items(self):
        self.assertEqual(self.dc.items.__len__(), 10)

    def test_should_connect_two_elements(self):
        self.dc.union(4, 3)
        self.assertTrue(self.dc.connected(4, 3))
        self.dc.union(6, 5)
        self.assertTrue(self.dc.connected(6, 5))
        self.dc.union(2, 1)
        self.assertTrue(self.dc.connected(2, 1))


    def test_should_connect_two_elements_between_others(self):
        self.dc.union(4, 3)
        self.dc.union(3, 8)
        self.assertTrue(self.dc.connected(4, 8))
        self.dc.union(9, 4)
        self.assertTrue(self.dc.connected(9, 3))


if __name__ == "__main__":
    unittest.main()

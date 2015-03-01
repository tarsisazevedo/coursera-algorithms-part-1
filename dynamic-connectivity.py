# encoding: utf-8

import unittest


class DynamicConectivity(object):
    def __init__(self, items):
        self.items = range(items)
        self.size = [1 for i in range(items)]

    # cada elemento referencia o pai, montando uma arvore.
    # a arvore é balanceada sempre colocando a menor diretamente na raiz da maior arvore.
    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.items[i] = j
            self.size[j] += self.size[i]
        else:
            self.items[j] = i
            self.size[i] += self.size[j]

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def _root(self, i):
        while (i != self.items[i]):
            self.items[i] = self.items[self.items[i]]
            i = self.items[i]
        return i


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

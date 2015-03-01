import unittest

def binary_search(_list, item):
    low_end = 0
    hi_end = len(_list) - 1

    while (low_end <= hi_end):
        mid = low_end + (hi_end - low_end) / 2
        if item < _list[mid]:
            hi_end = mid - 1
        elif item > _list[mid]:
            low_end = mid + 1
        else:
            return mid
    return -1


class BinarySearchTestCase(unittest.TestCase):
    def test_binary_search(self):
        _list = range(10)
        item = 3
        index = binary_search(_list, item)
        self.assertEqual(index, _list.index(item))

    def test_item_not_found(self):
        _list = range(10)
        item = 10
        index = binary_search(_list, item)
        self.assertEqual(index, -1)


if __name__ == "__main__":
    unittest.main()

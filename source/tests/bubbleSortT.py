import unittest
from source.algos.sorting.bubbleSort import bSort

class BubbleSortTest(unittest.TestCase):
    def setUp(self):
        self.arr = [5, 1, 56, 13]
        self.sort = bSort(self.arr)

    def test_sort(self):
        result = self.sort.sort()
        self.assertEqual([1, 5, 13, 56], result)

if __name__ == '__main__':
    unittest.main()
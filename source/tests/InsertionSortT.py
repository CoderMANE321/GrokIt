import unittest
from source.algos.sorting.insertionSort import sort

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.sorter = sort()

    def test_sorted_list(self):
        self.assertEqual(self.sorter.insertion([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_list(self):
        self.assertEqual(self.sorter.insertion([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(self.sorter.insertion([3, 1, 4, 2]), [1, 2, 3, 4])

    def test_list_with_duplicates(self):
        self.assertEqual(self.sorter.insertion([4, 2, 2, 3, 1]), [1, 2, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(self.sorter.insertion([]), [])

    def test_single_element_list(self):
        self.assertEqual(self.sorter.insertion([42]), [42])

if __name__ == '__main__':
    unittest.main()

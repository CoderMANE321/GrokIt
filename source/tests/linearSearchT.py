import unittest
from source.algos.searching.linearSearch import linearSearch


arr = [0, 1, 10, 18, 45]
new_search = linearSearch()
target = 10
non_existing = 20

class TestSearch(unittest.TestCase):
    def test_search(self):
        self.assertTrue(new_search.search(arr, target))
        self.assertFalse(new_search.search(arr, non_existing))

if __name__ == '__main__':
    unittest.main()

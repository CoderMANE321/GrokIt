import unittest
from source.structs.SegmentTree import ST

class TestSegmentTree(unittest.TestCase):
    def setUp(self):
        self.nums = [1, 3, 5, 7, 9, 11]
        self.tree = ST(self.nums)

    def test_initial_query(self):
        self.assertEqual(self.tree.query(0, 2), 9)   # 1 + 3 + 5
        self.assertEqual(self.tree.query(1, 3), 15)  # 3 + 5 + 7
        self.assertEqual(self.tree.query(3, 5), 27)  # 7 + 9 + 11
        self.assertEqual(self.tree.query(0, 5), 36)  # full range

    def test_update(self):
        self.tree.update(1, 10)  # Change nums[1] from 3 -> 10
        self.assertEqual(self.tree.query(0, 2), 16)  # 1 + 10 + 5
        self.assertEqual(self.tree.query(1, 3), 22)  # 10 + 5 + 7
        self.assertEqual(self.tree.query(0, 5), 43)  # Updated total

    def test_query_single_element(self):
        self.assertEqual(self.tree.query(4, 4), 9)
        self.tree.update(4, 100)
        self.assertEqual(self.tree.query(4, 4), 100)

if __name__ == '__main__':
    unittest.main()

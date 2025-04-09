import unittest
from source.structs.Heaps.MedianHeap import MedianHeap

class TestMedianHeap(unittest.TestCase):
    def test_push_and_top(self):
        mh = MedianHeap()
        nums = [5, 3, 8, 1, 6]
        expected_medians = [5, 4, 5, 4, 5]

        for i, num in enumerate(nums):
            mh.push(num)
            self.assertEqual(mh.top(), expected_medians[i])

    def test_pop(self):
        mh = MedianHeap()
        for num in [10, 20, 30]:
            mh.push(num)

        self.assertEqual(mh.pop(), 20)
        self.assertEqual(mh.top(), 20)  # New median after pop
        self.assertEqual(mh.pop(), 10)
        self.assertEqual(mh.pop(), 30)
        self.assertEqual(mh.top(), -1)

    def test_heapify(self):
        mh = MedianHeap()
        mh.heapify([2, 4, 6, 8])
        self.assertEqual(mh.top(), 5)

    def test_len(self):
        mh = MedianHeap()
        self.assertEqual(len(mh), 0)
        mh.push(1)
        self.assertEqual(len(mh), 1)
        mh.push(2)
        self.assertEqual(len(mh), 2)

if __name__ == '__main__':
    import unittest
    unittest.main()

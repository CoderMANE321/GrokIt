import unittest
from source.structs.Heaps.MaxHeap import MaxHeap

class TestMaxHeap(unittest.TestCase):
    def test_push_and_top(self):
        heap = MaxHeap()
        heap.push(5)
        self.assertEqual(heap.top(), 5)
        heap.push(10)
        self.assertEqual(heap.top(), 10)
        heap.push(3)
        self.assertEqual(heap.top(), 10)

    def test_pop(self):
        heap = MaxHeap()
        heap.push(7)
        heap.push(4)
        heap.push(9)
        heap.push(1)
        self.assertEqual(heap.pop(), 9)
        self.assertEqual(heap.pop(), 7)
        self.assertEqual(heap.pop(), 4)
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), -1)

    def test_heapify(self):
        heap = MaxHeap()
        heap.heapify([3, 1, 4, 1, 5, 9, 2])
        self.assertEqual(heap.pop(), 9)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 4)
        self.assertEqual(heap.pop(), 3)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), -1)

    def test_top_on_empty(self):
        heap = MaxHeap()
        self.assertEqual(heap.top(), -1)

if __name__ == '__main__':
    unittest.main()

import unittest
from source.structs.Heaps.MinHeap import MinHeap

class TestMinHeap(unittest.TestCase):
    def test_push_and_top(self):
        heap = MinHeap()
        heap.push(5)
        self.assertEqual(heap.top(), 5)
        heap.push(3)
        self.assertEqual(heap.top(), 3)
        heap.push(4)
        self.assertEqual(heap.top(), 3)

    def test_pop(self):
        heap = MinHeap()
        heap.push(10)
        heap.push(1)
        heap.push(5)
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 10)
        self.assertEqual(heap.pop(), -1)  # Empty heap

    def test_heapify(self):
        heap = MinHeap()
        heap.heapify([9, 4, 7, 1, -2, 6])
        self.assertEqual(heap.pop(), -2)
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), 4)
        self.assertEqual(heap.pop(), 6)
        self.assertEqual(heap.pop(), 7)
        self.assertEqual(heap.pop(), 9)
        self.assertEqual(heap.pop(), -1)  # Heap is empty

    def test_top_on_empty(self):
        heap = MinHeap()
        self.assertEqual(heap.top(), -1)

    def test_single_element(self):
        heap = MinHeap()
        heap.push(42)
        self.assertEqual(heap.top(), 42)
        self.assertEqual(heap.pop(), 42)
        self.assertEqual(heap.pop(), -1)

if __name__ == '__main__':
    unittest.main()

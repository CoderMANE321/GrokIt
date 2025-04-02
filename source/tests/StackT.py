import unittest
from source.structs.Stack import Stack

class StackTests(unittest.TestCase):
    def setUp(self):
            self.s = Stack()

    def test_push(self):
        self.s.push(1)
        self.s.push(5)
        self.assertEqual(self.s.getVals(), [1, 5])

    def test_pop(self):
        self.s.push(1)
        self.s.push(5)
        self.s.push(6)
        result = self.s.pop()
        self.assertEqual(result, 6)
        self.assertEqual(self.s.getVals(), [1, 5])

    def test_peek(self):
        self.s.push(1)
        self.s.push(5)
        result = self.s.peek()
        self.assertEqual(result, 5)
        self.assertEqual(self.s.getVals(), [1, 5])

    def test_getVals(self):
        self.s.push(1)
        self.s.push(5)
        self.s.push(56)
        self.s.push(34)
        self.assertEqual(self.s.getVals(), [1, 5, 56, 34])

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.s.pop()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.s.peek()

if __name__ == '__main__':
    unittest.main()

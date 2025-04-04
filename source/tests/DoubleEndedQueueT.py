import unittest
from source.structs.DoubleEndedQueue import Deque

class TestDeque(unittest.TestCase):
    def setUp(self):
        self.dq = Deque()

    def test_isEmpty(self):
        self.assertTrue(self.dq.isEmpty())
        self.dq.append(1)
        self.assertFalse(self.dq.isEmpty())

    def test_append_and_pop(self):
        self.dq.append(10)
        self.dq.append(20)
        self.assertEqual(self.dq.pop(), 20)
        self.assertEqual(self.dq.pop(), 10)
        self.assertEqual(self.dq.pop(), -1)  # Edge case: Empty deque

    def test_appendleft_and_popleft(self):
        self.dq.appendleft(30)
        self.dq.appendleft(40)
        self.assertEqual(self.dq.popleft(), 40)
        self.assertEqual(self.dq.popleft(), 30)
        self.assertEqual(self.dq.popleft(), -1)  # Edge case: Empty deque

    def test_mixed_operations(self):
        self.dq.append(1)
        self.dq.appendleft(2)
        self.dq.append(3)
        self.dq.appendleft(4)

        self.assertEqual(self.dq.popleft(), 4)
        self.assertEqual(self.dq.pop(), 3)
        self.assertEqual(self.dq.popleft(), 2)
        self.assertEqual(self.dq.pop(), 1)
        self.assertEqual(self.dq.pop(), -1)  # Edge case

if __name__ == '__main__':
    unittest.main()
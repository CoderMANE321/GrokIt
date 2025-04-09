import unittest
from source.structs.HashTable import Hash

class TestHashTable(unittest.TestCase):

    def test_insert_and_get(self):
        h = Hash(4)
        h.insert(1, 10)
        h.insert(2, 20)
        self.assertEqual(h.get(1), 10)
        self.assertEqual(h.get(2), 20)
        self.assertEqual(h.get(3), -1)  # Not inserted

    def test_update_value(self):
        h = Hash(4)
        h.insert(1, 10)
        h.insert(1, 100)  # Update value
        self.assertEqual(h.get(1), 100)

    def test_remove(self):
        h = Hash(4)
        h.insert(1, 10)
        h.insert(2, 20)
        removed = h.remove(1)
        self.assertTrue(removed)
        self.assertEqual(h.get(1), -1)
        self.assertFalse(h.remove(99))  # Non-existent key

    def test_resize(self):
        h = Hash(2)
        h.insert(1, 10)
        h.insert(2, 20)  # Should trigger resize here (50% load factor)
        h.insert(3, 30)
        self.assertTrue(h.getCapacity() > 2)
        self.assertEqual(h.get(1), 10)
        self.assertEqual(h.get(2), 20)
        self.assertEqual(h.get(3), 30)

    def test_collision_and_chaining(self):
        h = Hash(2)
        h.insert(0, 10)
        h.insert(2, 20)  # Collides with key 0
        self.assertEqual(h.get(0), 10)
        self.assertEqual(h.get(2), 20)

    def test_size_tracking(self):
        h = Hash(4)
        self.assertEqual(h.getSize(), 0)
        h.insert(1, 10)
        h.insert(2, 20)
        self.assertEqual(h.getSize(), 2)
        h.remove(1)
        self.assertEqual(h.getSize(), 1)

if __name__ == '__main__':
    unittest.main()

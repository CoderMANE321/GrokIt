import unittest

from source.structs.BinarySearchTree import Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.insert(5, 50)
        self.tree.insert(3, 30)
        self.tree.insert(7, 70)
        self.tree.insert(2, 20)
        self.tree.insert(4, 40)
        self.tree.insert(6, 60)
        self.tree.insert(8, 80)

    def test_get(self):
        self.assertEqual(self.tree.get(5), 50)
        self.assertEqual(self.tree.get(3), 30)
        self.assertEqual(self.tree.get(99), -1)

    def test_getMin_getMax(self):
        self.assertEqual(self.tree.getMin(), 20)
        self.assertEqual(self.tree.getMax(), 80)

    def test_getInorderKeys(self):
        self.assertEqual(self.tree.getInorderKeys(), [2, 3, 4, 5, 6, 7, 8])

    def test_remove_leaf(self):
        self.tree.remove(2)
        self.assertEqual(self.tree.getInorderKeys(), [3, 4, 5, 6, 7, 8])

    def test_remove_one_child(self):
        self.tree.remove(2)
        self.tree.remove(3)
        self.assertEqual(self.tree.getInorderKeys(), [4, 5, 6, 7, 8])

    def test_remove_two_children(self):
        self.tree.remove(2)
        self.tree.remove(3)
        self.tree.remove(5)
        self.assertEqual(self.tree.getInorderKeys(), [4, 6, 7, 8])

    def test_remove_all(self):
        keys = [2, 3, 4, 5, 6, 7, 8]
        for key in keys:
            self.tree.remove(key)
        self.assertEqual(self.tree.getInorderKeys(), [])
        self.assertEqual(self.tree.getMin(), -1)
        self.assertEqual(self.tree.getMax(), -1)

if __name__ == '__main__':
    unittest.main()


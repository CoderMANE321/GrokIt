import unittest
from source.structs.DisjointSet import UnionFind

class TestUnionFind(unittest.TestCase):
    def test_initial_components(self):
        uf = UnionFind(5)
        self.assertEqual(uf.getNumComponents(), 5)
        for i in range(5):
            self.assertTrue(uf.isSameComponent(i, i))

    def test_union_and_find(self):
        uf = UnionFind(5)
        self.assertTrue(uf.union(0, 1))
        self.assertTrue(uf.isSameComponent(0, 1))
        self.assertEqual(uf.getNumComponents(), 4)

        self.assertTrue(uf.union(1, 2))
        self.assertTrue(uf.isSameComponent(0, 2))
        self.assertEqual(uf.getNumComponents(), 3)

    def test_redundant_union(self):
        uf = UnionFind(3)
        uf.union(0, 1)
        self.assertFalse(uf.union(0, 1))  # Already connected
        self.assertEqual(uf.getNumComponents(), 2)

    def test_multiple_unions(self):
        uf = UnionFind(6)
        uf.union(0, 1)
        uf.union(2, 3)
        uf.union(4, 5)
        uf.union(0, 2)
        uf.union(0, 4)
        self.assertTrue(uf.isSameComponent(1, 5))
        self.assertEqual(uf.getNumComponents(), 1)

if __name__ == "__main__":
    unittest.main()

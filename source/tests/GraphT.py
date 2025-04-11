import unittest
from source.structs.Graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_edge(self):
        self.graph.addEdge(1, 2)
        self.assertIn(2, self.graph.adj_list[1])
        self.assertIn(1, self.graph.adj_list)
        self.assertIn(2, self.graph.adj_list)

    def test_remove_edge(self):
        self.graph.addEdge(1, 2)
        self.assertTrue(self.graph.removeEdge(1, 2))
        self.assertFalse(self.graph.removeEdge(1, 2))  # Already removed

    def test_has_path_direct(self):
        self.graph.addEdge(1, 2)
        self.assertTrue(self.graph.hasPath(1, 2))

    def test_has_path_indirect(self):
        self.graph.addEdge(1, 2)
        self.graph.addEdge(2, 3)
        self.assertTrue(self.graph.hasPath(1, 3))

    def test_has_path_none(self):
        self.graph.addEdge(1, 2)
        self.graph.addEdge(3, 4)
        self.assertFalse(self.graph.hasPath(1, 4))

    def test_has_path_cycle(self):
        self.graph.addEdge(1, 2)
        self.graph.addEdge(2, 3)
        self.graph.addEdge(3, 1)
        self.assertTrue(self.graph.hasPath(1, 3))
        self.assertTrue(self.graph.hasPath(3, 2))

    def test_has_path_self_loop(self):
        self.graph.addEdge(1, 1)
        self.assertTrue(self.graph.hasPath(1, 1))

if __name__ == "__main__":
    unittest.main()

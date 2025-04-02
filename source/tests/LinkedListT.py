import unittest
from source.structs.LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
    
    def test_insert_head(self):
        self.ll.insertHead(10)
        self.ll.insertHead(20)
        self.assertEqual(self.ll.getValues(), [20, 10])
    
    def test_insert_tail(self):
        self.ll.insertTail(30)
        self.ll.insertTail(40)
        self.assertEqual(self.ll.getValues(), [30, 40])
    
    def test_get(self):
        self.ll.insertHead(5)
        self.ll.insertHead(15)
        self.assertEqual(self.ll.get(0), 15)
        self.assertEqual(self.ll.get(1), 5)
        self.assertEqual(self.ll.get(2), -1)
    
    def test_remove(self):
        self.ll.insertHead(1)
        self.ll.insertHead(2)
        self.ll.insertHead(3)
        self.assertTrue(self.ll.remove(1))
        self.assertEqual(self.ll.getValues(), [3, 1])
        self.assertFalse(self.ll.remove(5))
    
    def test_empty_list(self):
        self.assertEqual(self.ll.get(0), -1)
        self.assertFalse(self.ll.remove(0))
        self.assertEqual(self.ll.getValues(), [])
    
    def test_single_element_list(self):
        self.ll.insertHead(99)
        self.assertEqual(self.ll.getValues(), [99])
        self.assertTrue(self.ll.remove(0))
        self.assertEqual(self.ll.getValues(), [])
        self.assertEqual(self.ll.get(0), -1)
        self.assertFalse(self.ll.remove(0))

if __name__ == "__main__":
    unittest.main()
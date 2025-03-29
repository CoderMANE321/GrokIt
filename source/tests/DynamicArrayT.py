import unittest
from source.structs.DynamicArray import Array

dynamic_array = Array(10)

class ArrayTest(unittest.TestCase):
    def test_get(self):
        dynamic_array.set(0, 5)
        self.assertEqual(dynamic_array.get(0), 5)

    def test_set(self):
        dynamic_array.set(1, 10)
        self.assertEqual(dynamic_array.get(1), 10)

    def test_pushback(self):
        initial_size = dynamic_array.getSize()
        dynamic_array.pushback(20)
        self.assertEqual(dynamic_array.get(dynamic_array.getSize() - 1), 20)
        self.assertEqual(dynamic_array.getSize(), initial_size + 1)

    def test_popback(self):
        dynamic_array.pushback(30)
        last_value = dynamic_array.popback()
        self.assertEqual(last_value, 30)
        self.assertEqual(dynamic_array.getSize(), 1)

    def test_resize(self):
        for i in range(10):
            dynamic_array.pushback(i)
        initial_capacity = dynamic_array.getCapacity()
        dynamic_array.pushback(100) 
        self.assertGreater(dynamic_array.getCapacity(), initial_capacity)
        self.assertEqual(dynamic_array.get(dynamic_array.getSize() - 1), 100)

    def test_get_size(self):
        self.assertEqual(dynamic_array.getSize(), len([x for x in dynamic_array.arr if x != 0]))

    def test_get_capacity(self):
        self.assertGreaterEqual(dynamic_array.getCapacity(), dynamic_array.getSize())

if __name__ == '__main__':
    unittest.main()

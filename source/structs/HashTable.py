class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class Hash:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity


    def hash_function(self, key: int):
        return key % self.capacity
    

    def insert(self, key: int, value: int):
        index = self.hash_function(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        return -1


    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next

        return False


    def getSize(self) -> int:
        return self.size
    
    
    def getCapacity(self) -> int:
        return self.capacity
    

    def resize(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            while node:
                index = node.key % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next 
                    new_node.next = Node(node.key, node.value)
                node = node.next

        self.table = new_table
        self.capacity = new_capacity
             


'''
Time Complexity:
- insert:    O(1) average, O(n) worst-case (due to collisions and potential resize)
- get:       O(1) average, O(n) worst-case (if many collisions)
- remove:    O(1) average, O(n) worst-case (if many collisions)
- resize:    O(n), where n is the number of elements (each rehashed once)

Space Complexity:
- O(n + m), where:
    - n = number of key-value pairs stored (Node instances)
    - m = current capacity of the table (size of array)
'''
    


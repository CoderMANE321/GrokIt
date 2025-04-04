class Node:
    def __init__(self, value: int = 0):
        self.value = value
        self.next: "Node | None" = None
        self.prev: "Node | None" = None

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next is self.tail

    def append(self, value: int):
        newNode = Node(value)
        last_node = self.tail.prev

        last_node.next = newNode
        newNode.prev = last_node
        newNode.next = self.tail
        self.tail.prev = newNode

    def appendleft(self, value: int):
        newNode = Node(value)
        first_node = self.head.next

        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = first_node
        first_node.prev = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        last_node = self.tail.prev
        value = last_node.value
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        first_node = self.head.next
        value = first_node.value
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value
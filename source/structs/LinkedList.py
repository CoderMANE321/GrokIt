from typing import List

class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        if self.head.next is None:
            self.head.next = new_node

    def remove(self, index: int) -> bool:
        prev = self.head
        curr = self.head.next
        i = 0
        
        while curr:
            if i == index:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                return True
            prev, curr = curr, curr.next
            i += 1
        
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values



'''
Time Complexity: O(1) 
get()  -> O(n) traverses whole list
insertHead() -> O(1) replaces head with newNode
insertTail() -> O(1) pointer enables swap with current and new tail
remove() -> O(n) traverses until index is found for swap
getValues() -> O(n) traverses array for vals to append into list

Space complexity: O(1)
get() -> O(1) no new memory allocated 
insertHead/Tail() -> O(1) new node allocated only
remove() -> O(1) new new memory allocated
getValues() -> O(n) each node most be appended to list
'''
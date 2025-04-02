class Stack:
    def __init__(self):
        self.stack = []

    def push(self, i: int):
        self.stack.append(i)

    def pop(self) -> int:
        if not self.stack:
            raise IndexError("pop from empty stack") 
        return self.stack.pop(-1)

    def peek(self) -> int:
        if not self.stack:
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def getVals(self):
        return self.stack

"""
Space Complexity: O(n) - We store up to 'n' elements in the stack.

Time Complexity:
- push(i)  : O(n)  (Because insert(0, i) shifts all elements)
- pop()    : O(n)  (Because pop(0) shifts all elements)
- peek()   : O(1)  (Accessing the first element)
- getVals(): O(1)  (Returning a reference to the list)
"""

from typing import List

class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int):
        newNode = Node(key, val)
        if not self.root:
            self.root = newNode
            return 0

        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = newNode
                    return 0
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = newNode
                    return 0
                curr = curr.right
            else:
                # If key exists, overwrite
                curr.val = val
                return 0

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key == curr.key:
                return curr.val
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int):
        self.root = self._remove(self.root, key)

    def _remove(self, node: Node, key: int):
        if not node:
            return None

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # Node found
            if not node.left and not node.right:
                return None
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Two children: get in-order successor
            succ = self._getMinNode(node.right)
            node.key = succ.key
            node.val = succ.val
            node.right = self._remove(node.right, succ.key)
        return node

    def _getMinNode(self, node: Node):
        while node.left:
            node = node.left
        return node

    def getInorderKeys(self) -> List[int]:
        return self._dfs(self.root)

    def _dfs(self, node: Node) -> List[int]:
        if not node:
            return []
        return self._dfs(node.left) + [node.key] + self._dfs(node.right)



'''
Time Complexity Summary:
- insert: O(h)
- get: O(h)
- getMin / getMax: O(h)
- remove: O(h)
- getInorderKeys: O(n)

Space Complexity Summary:
- insert/get/getMin/getMax: O(1)
- remove: O(h) due to recursion
- getInorderKeys: O(n) for recursion + result list

Note:
In a balanced BST, h = log(n), so these become O(log n).
In a worst-case unbalanced BST (e.g., like a linked list), h = n, so worst case is O(n).
'''
from typing import List

class MaxHeap:
    def __init__(self):
        self.heap = [0]


    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return root


    def top(self) -> int:
        if len(self.heap) <= 1:
            return -1
        return self.heap[1]


    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self._bubble_down(i)


    def _bubble_up(self, index: int) -> None:
        parent = index // 2
        while index > 1 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index // 2


    def _bubble_down(self, index: int) -> None:
        child = 2 * index
        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child] < self.heap[child + 1]:
                child += 1

            if self.heap[child] <= self.heap[index]:
                break

            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child = 2 * index

    def __len__(self):
        return len(self.heap) - 1  # subtract the dummy 0



'''
Time Complexity:
- push(val): O(log n) 
    In the worst case, the inserted element bubbles up to the root.
- pop(): O(log n)
    In the worst case, the new root bubbles down to the leaf level.
- top(): O(1)
    Constant time to access the root element.
- heapify(nums): O(n)
    Builds the heap in-place using bottom-up heapification. More efficient than inserting each element (O(n log n)).

Space Complexity:
- Overall: O(n)
    The heap is stored as an array of size n+1 (with a dummy 0 at index 0).
- Each method: O(1) auxiliary space
    No extra data structures are used during operations; all actions are done in-place.
'''
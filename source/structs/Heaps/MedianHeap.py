from typing import List
from source.structs.Heaps.MaxHeap import MaxHeap
from source.structs.Heaps.MinHeap import MinHeap

class MedianHeap:
    def __init__(self):
        self._max = MaxHeap()  # holds the smaller half (as max-heap)
        self._min = MinHeap()  # holds the larger half (as min-heap)

    def push(self, val: int) -> None:
        if self._max.top() == -1 or val <= self._max.top():
            self._max.push(val)
        else:
            self._min.push(val)

        # Rebalance: max heap can have 1 more element than min heap
        if len(self._max) > len(self._min) + 1:
            self._min.push(self._max.pop())
        elif len(self._min) > len(self._max):
            self._max.push(self._min.pop())

    def top(self) -> int:
        if len(self._max) > len(self._min):
            return self._max.top()
        return (self._max.top() + self._min.top()) // 2

    def pop(self) -> int:
        if len(self._max) >= len(self._min):
            return self._max.pop()
        return self._min.pop()

    def heapify(self, nums: List[int]) -> None:
        for num in nums:
            self.push(num)

    def __len__(self):
        return len(self._max) + len(self._min)


'''
Time Complexity:
- push(val): O(log n) – inserting into either heap and possibly rebalancing
- top(): O(1) – just reading root(s)
- pop(): O(log n) – removing from heap and possibly rebalancing
- heapify(nums): O(n log n) – each push is O(log n)

Space Complexity:
- Overall: O(n) – storing n elements in two heaps
- Auxiliary space: O(1) – all heap operations are in-place
'''

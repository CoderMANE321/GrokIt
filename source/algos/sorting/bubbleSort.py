from typing import List

class bSort:
    def __init__(self, arr: List[int]):
        self.arr = arr

    def sort(self) -> List[int]:
        _len = len(self.arr)
        for i in range(_len):
            swapped = False
            for j in range(_len - 1 - i):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    swapped = True
            if not swapped:
                break
        return self.arr

        


"""
Space Complexity: O(1)
no new objects allocated in heap

Time Complexity: O(n**2)
nested loops are n squared n/2 * 2 = O(n**2)
"""
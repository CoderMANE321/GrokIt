from typing import List

class quickSort:
    def __init__(self):
        pass

    def Sort(self, arr: list[int], s: int, e: int) -> list[int]:
        if e - s + 1 <= 1:
            return arr
        
        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        arr[e] = arr[left]
        arr[left] = pivot

        quickSort(arr, s, left - 1)
        quickSort(arr, left + 1, e)

        return arr
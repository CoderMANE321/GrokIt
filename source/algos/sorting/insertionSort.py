class sort:
    def  __init__(self):
        pass

    def insertion(self, arr):
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0 and arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                j -= 1
        return arr



'''
Time:
insertion -> O(n**2) nested loop
Space:
O(1) -> in place modification
'''
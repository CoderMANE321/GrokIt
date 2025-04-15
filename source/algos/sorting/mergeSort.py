class Sort:
    def __init__(self):
        pass

    def helper(self, arr):
        if len(arr) <= 1:
            return arr 

        mid = len(arr) // 2
        left = self.helper(arr[:mid])
        right = self.helper(arr[mid:])

        return self.helper(left, right)
        

    def merge_sort(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
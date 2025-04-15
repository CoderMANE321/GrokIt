from source.algos.sorting.mergeSort import Sort


merge_sort = Sort()
arr = [5, 4, 3, 2, 1]
result = merge_sort.helper(arr)
merge_sort.merge_sort(result)

assert(arr, [1, 2, 3, 4, 5])

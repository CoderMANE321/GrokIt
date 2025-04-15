from source.algos.sorting.quickSort import quickSort

quick_sort = quickSort()
arr = [5, 4, 3, 2, 1]
quick_sort.Sort(arr , 0, 4)

assert(arr, [1, 2, 3, 4, 5])

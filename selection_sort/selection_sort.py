def selection_sort(arr):
    # TODO: Implement selection sort
    n = len(arr)
    for i in range(n):
        # Assume the current index is the minimum
        min_index = i
        # Find the index of the smallest element in the remaining list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap if a smaller element was found
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

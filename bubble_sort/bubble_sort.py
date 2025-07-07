def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    n = len(unsorted_list)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        if not swapped:
            break
    return unsorted_list

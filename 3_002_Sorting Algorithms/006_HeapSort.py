#%% Imports and function declaration


def heapsort(arr):
    arr_sorted = []

    # Create the Max Heap
    for i in range(len(arr)):
        arr = heapify(arr, i)

    # Swaper
    swap_position = len(arr)-1

    for i in range(len(arr)-1):
        bigger_value = arr[0]
        # Swap biggest value <-> Last maxheap value
        arr[0] = arr[swap_position]
        arr[swap_position] = bigger_value

        # Max-heapify
        for i in range(swap_position):
            arr = heapify(arr, i)

        swap_position -= 1  # Freeze last array position
    return arr


def heapify(arr, index):
    """
    :param: arr - array to heapify
    i -- index of the current node
    """

    if index == 0:  # End of heap
        return arr

    index_parent = (index - 1)//2
    value_parent = arr[index_parent]
    value_children = arr[index]

    if value_children > value_parent:  # Switch parent <-> children
        arr[index_parent] = value_children  # Parent Update
        arr[index] = value_parent  # Children Update
        arr = heapify(arr, index_parent)

    else:  # No swap required
        pass

    return arr


#%% Testing Official
arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
assert heapsort(arr) == solution

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
assert heapsort(arr) == solution

arr = [99]
solution = [99]
assert heapsort(arr) == solution

arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
assert heapsort(arr) == solution
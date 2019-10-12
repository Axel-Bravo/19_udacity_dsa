# Solution
def last_index(arr, target):
    # we start looking from the last index
    return last_index_arr(arr, target, len(arr) - 1)


def last_index_arr(arr, target, index):
    if index < 0:
        return -1
    
    # check if target is found
    if arr[index] == target:
        return index

    # else make a recursive call to the rest of the array
    return last_index_arr(arr, target, index - 1)
#%% Import and function declaracion
def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    """
    if len(arr) == 1:
        if arr[0] == target:
            return 0
        else:
            return -1
    else:
        prev_lvl = last_index(arr=arr[1:], target=target)
        curr_lvl = arr[0]

        if (prev_lvl == -1) & (curr_lvl != target):
            return -1

        return prev_lvl + 1





#%% Testing
arr = [1, 2, 5, 5, 4]
target = 5
solution = 3
print(last_index(arr, target))

arr = [1, 2, 5, 5, 4]
target = 7
solution = -1
print(last_index(arr, target))

arr = [91, 19, 3, 8, 9]
target = 91
solution = 0
print(last_index(arr, target))


arr = [1, 1, 1, 1, 1, 1]
target = 1
solution = 5
print(last_index(arr, target))
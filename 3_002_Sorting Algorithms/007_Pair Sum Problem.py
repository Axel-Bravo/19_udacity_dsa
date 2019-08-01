#%% Imports and functions declaration
def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    Return the two numbers in the form of a sorted list
    """

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                if arr[i] > arr[j]:
                    return [arr[j], arr[i]]
                else:
                    return [arr[i], arr[j]]

    return [None, None]


#%% Testing - DEV

input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
assert pair_sum(input_list, target) == solution, "Not passed"

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
assert pair_sum(input_list, target) == solution, "Not passed"

input_list = [110, 9, 89]
target = 9
solution = [None, None]
assert pair_sum(input_list, target) == solution, "Not passed"

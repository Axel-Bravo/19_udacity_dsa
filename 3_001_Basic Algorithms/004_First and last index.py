#%% Imports and function declaration
def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center + 1:], left + center + 1)
    else:
        return recursive_binary_search(target, source[:center], left)


def first_and_last_index(source, target):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    initial_index = recursive_binary_search(target, source)

    if initial_index is None:
        return [-1, -1]

    # Search lowerbound
    lower_index = initial_index
    while source[lower_index] == target:
        if lower_index == 0:
            lower_index = 0
            break
        if source[lower_index - 1] == target:
            lower_index -= 1
        else:
            break

    # Search upperbound
    upper_index = initial_index
    while source[upper_index] == target:
        if upper_index == len(source) - 1:
            upper_index = len(source) - 1
            break
        if source[upper_index + 1] == target:
            upper_index += 1
        else:
            break

    return [lower_index, upper_index]


#%% Testing
input_list = [1]
number = 1
print(first_and_last_index(input_list, number))
# solution = [0, 0]

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
print(first_and_last_index(input_list, number))
# solution = [3, 6]

input_list = [0, 1, 2, 3, 4, 5]
number = 5
print(first_and_last_index(input_list, number))
# solution = [5, 5]

input_list = [0, 1, 2, 3, 4, 5]
number = 6
print(first_and_last_index(input_list, number))
# solution = [-1, -1]
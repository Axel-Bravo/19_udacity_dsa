#%% Imports and  function declaration
from math import floor


def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index + 1
    elif target < mid_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)


def binary_search_recursive(array, target, index_ref):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    if len(array) == 1:
        if array[0] == target:
            return index_ref
        else:
            return -1

    center_list = floor((len(array)-1)/2)

    if center_list * 2 < len(array):
        index_ref = index_ref - center_list - 1
    else:
        index_ref = index_ref - center_list

    if target == array[center_list]:
        return index_ref
    elif target < array[center_list]:
        index_target = binary_search_recursive(array[:center_list], target, index_ref)

    else:
        index_target = binary_search_recursive(array[center_list:], target, index_ref)

    return index_target


#%% Testing
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 5

assert binary_search_recursive(array, target, len(array)) == index, "Not correct own implementation"
assert binary_search_recursive_soln(array, target, 0, len(array)) == index, "Not correct Udacity implementation"


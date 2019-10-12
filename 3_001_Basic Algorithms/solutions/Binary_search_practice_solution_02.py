def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
    
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)
        
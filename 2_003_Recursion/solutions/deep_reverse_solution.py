def is_list(element):
    """
    Check if element is a Python list
    """
    return isinstance(element, list)

def deep_reverse(arr):
    """
    Function to deep_reverse an input list
    """
    return deep_reverse_func(arr, 0)

def deep_reverse_func(arr, index):
    """
    Recursive function to deep_reverse the input list
    """
    # Base Case
    if index == len(arr):
        return list()
    
    output = deep_reverse_func(arr, index + 1)
    
    # if element is a list --> deep_reverse the list
    if is_list(arr[index]):
        to_append = deep_reverse(arr[index])
    else:
        to_append = arr[index]
        
    output.append(to_append)
    return output
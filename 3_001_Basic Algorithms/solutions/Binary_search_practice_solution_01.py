def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1
    
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2        # integer division in Python 3
        
        mid_element = array[mid_index]
        
        if target == mid_element:                       # we have found the element
            return mid_index
        
        elif target < mid_element:                      # the target is less than mid element
            end_index = mid_index - 1                   # we will only search in the left half
        
        else:                                           # the target is greater than mid element
            start_index = mid_element + 1               # we will search only in the right half
    
    return -1
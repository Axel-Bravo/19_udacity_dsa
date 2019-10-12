# Solution

def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.

    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    sorted_array = []
    
    linked_list = SortedLinkedList()
    for value in array:
        linked_list.append(value)
    
    # Convert sorted linked list to a normal list/array
    node = linked_list.head
    while node:
        sorted_array.append(node.value)
        node = node.next
    
    return sorted_array

print ("Pass" if (sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")

# Solution

def swap_nodes(head, left_index, right_index):

    # if both the indices are same
    if left_index == right_index:
        return head
    
    
    left_previous = None
    left_current = None

    right_previous = None
    right_current = None

    count = 0
    temp = head
    new_head = None

    # find out previous and current node at both the indices
    while temp is not None:
        if count == left_index:
            left_current = temp
        elif count == right_index:
            right_current = temp
            break

        if left_current is None:
            left_previous = temp
        right_previous = temp
        temp = temp.next
        count += 1

    right_previous.next = left_current
    temp = left_current.next
    left_current.next = right_current.next

    # if both the indices are next to each other
    if left_index != right_index:
        right_current.next = temp

    # if the node at first index is head of the original linked list
    if left_previous is None:
        new_head = right_current
    else:
        left_previous.next = right_current
        new_head = head

    return new_head
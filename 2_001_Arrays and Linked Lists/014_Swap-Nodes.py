#%% Imports and function declaration
class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# Personal Implementation
def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: left_index - indicates position
    :param: right_index - indicates position
    return: head of updated linked list with nodes swapped
    Do not create a new linked list
    """
    # Values to swap
    node = head
    position = 0
    while position <= right_index:
        if position == left_index:
            left_data = node.data

        if position == right_index:
            right_data = node.data
        position += 1
        node = node.next

    # Swapping values
    node = head
    position = 0
    while position <= right_index:
        if position == left_index:
            node.data = right_data

        if position == right_index:
            node.data = left_data
        position += 1
        node = node.next

    return head


#%% Testing
# Case 1
arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 3
right_index = 4
head = create_linked_list(arr)
print_linked_list(swap_nodes(head=head, left_index=left_index, right_index=right_index))

# Case 2
arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2
right_index = 4
head = create_linked_list(arr)
print_linked_list(swap_nodes(head=head, left_index=left_index, right_index=right_index))

# Case 3
arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
head = create_linked_list(arr)
print_linked_list(swap_nodes(head=head, left_index=left_index, right_index=right_index))
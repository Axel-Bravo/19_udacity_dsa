#%% Imports and function declaration

class Node:
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
        print(head.data, end=' ')
        head = head.next
    print()


# Own implementation
def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """

    input_node = head
    trim_link_list = None

    position_counter = 1
    i_mode = True
    last_node = False

    while not last_node:
        if i_mode:  # Additive mode
            if trim_link_list is None:
                trim_link_list = Node(input_node.data)
            else:
                position_tail = trim_link_list
                while position_tail.next:  # Moving to the end of the list
                    position_tail = position_tail.next
                position_tail.next = Node(input_node.data)

            if position_counter == i:
                i_mode = False
                position_counter = 0

        else:  # Non-additive mode
            if position_counter == j:
                i_mode = True
                position_counter = 0

        position_counter += 1
        last_node = input_node.next is None
        input_node = input_node.next

    return trim_link_list


#%% Testing Zone

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]

tets = skip_i_delete_j(head, i, j)

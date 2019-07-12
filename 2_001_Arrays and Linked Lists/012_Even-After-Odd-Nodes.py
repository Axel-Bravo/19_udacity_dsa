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


# Functions developed
def even_number(number: int) -> bool:
    return number % 2 == 0


def list_updater(odd_num_list, even_num_list, number):
    if even_number(number):
        even_num_list.append(number)
    else:
        odd_num_list.append(number)
    return odd_num_list, even_num_list

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    linked_list_end = False
    even_linked_list = None
    odd_linked_list = None

    node = head

    while not linked_list_end:
        if node.data % 2 == 0:  # Even case
            if even_linked_list is None:
                even_linked_list = Node(node.data)
            else:
                position_tail = even_linked_list
                while position_tail.next:  # Moving to the end of the list
                    position_tail = position_tail.next

                position_tail.next = Node(node.data)

        else:  # Odd case
            if odd_linked_list is None:
                odd_linked_list = Node(node.data)
            else:
                position_tail = odd_linked_list
                while position_tail.next:  # Moving to the end of the list
                    position_tail = position_tail.next

                position_tail.next = Node(node.data)

        linked_list_end = node.next is None
        node = node.next

    position_tail = odd_linked_list
    while position_tail.next:  # Moving to the end of the list
        position_tail = position_tail.next
    position_tail.next = even_linked_list

    return odd_linked_list

#%% Testing
arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)

test = even_after_odd(head)
print_linked_list(test)

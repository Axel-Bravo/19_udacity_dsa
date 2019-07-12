#%%
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


# Personal implementations
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
    even_numbers = []
    odd_numbers = []

    node = head
    while node.next is not None:
        odd_numbers, even_numbers = list_updater(odd_num_list=odd_numbers,
                                                 even_num_list=even_numbers,
                                                 number=node.data)
        node = node.next

    odd_numbers, even_numbers = list_updater(odd_num_list=odd_numbers,
                                             even_num_list=even_numbers,
                                             number=node.data)

    all_numbers = [odd_numbers, even_numbers]
    all_numbers = [item for sublist in all_numbers for item in sublist]

    create_linked_list(all_numbers)

    return all_numbers


#%% Testing

arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)

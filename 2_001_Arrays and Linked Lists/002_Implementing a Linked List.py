
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def create_linked_list_me(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    try:
        head = Node(input_list.pop(0))

        while len(input_list) > 0:
            current_node = head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(input_list.pop(0))
    except IndexError:
        head = None

    return head


def create_linked_list_better_me(input_list):
    """
    Function to create a linked list, improved performance
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    try:
        head = Node(input_list.pop(0))
        tail = head

        while len(input_list) > 0:
            tail.next = Node(input_list.pop(0))
            tail = tail.next

    except IndexError:
        head = None

    return head


def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            # Move to the tail (the last node)
            current_node = head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(value)
    return head


if __name__ == '__main__':

    input_list = [1, 2, 3, 4, 5, 6]
    head_uc = create_linked_list(input_list)
    head_axel = create_linked_list_me(input_list)
    print('All finished')
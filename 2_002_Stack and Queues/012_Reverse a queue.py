#%% Imports and function declaration
class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def reverse_queue(queue):
    """
    Reverese the input queue

    Args:
       queue(queue),str2(string): Queue to be reversed
    Returns:
       queue: Reveresed queue
    """

    reversed_queue = Queue()
    remaining_num_elements = queue.num_elements

    while remaining_num_elements > 0:
        tail_head = queue.head
        i_counter = 1

        while i_counter < remaining_num_elements:
            tail_head = tail_head.next
            i_counter += 1

        reversed_queue.enqueue(tail_head.data)
        remaining_num_elements -= 1

    return reversed_queue


#%% Testing

test_case_1 = [1, 2, 3, 4]
queue = Queue()
for num in test_case_1:
    queue.enqueue(num)

test_case_1_reversed = reverse_queue(queue)


#%% Imports and functions declarations
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        """ Return the size or length of the linked list. """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        """Transforms the linked list content into a list"""
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


def union(linkedlist_1: LinkedList, linkedlist_2: LinkedList) -> list:
    """
    For two given linked list, returns all the values present in whichever, one time each value
    :param linkedlist_1: first linked list
    :param linkedlist_2: second linked list
    :return: set of all values
    """
    list_1 = linkedlist_1.to_list()
    list_2 = linkedlist_2.to_list()

    list_all = list(set(list_1 + list_2))

    linked_list = LinkedList()

    for i in list_all:
        linked_list.append(i)

    return linked_list


def intersection(linkedlist_1: LinkedList, linkedlist_2: LinkedList) -> list:
    """
    For two given linked list, returns all the values present in both lists, one time each value
    :param linkedlist_1: first linked list
    :param linkedlist_2: second linked list
    :return: set of all coincident values
    """
    set_1 = set(linkedlist_1.to_list())
    set_2 = set(linkedlist_2.to_list())

    common_set = []
    for element in set_1:
        if element in set_2:
            common_set.append(element)

    linked_list = LinkedList()

    for i in common_set:
        linked_list.append(i)

    return linked_list


#%% Test Official
# Normal Cases:
# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1, linked_list_2))
# 4 -> 6 -> 21 ->

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print(intersection(linked_list_3, linked_list_4))
#

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [22, 7, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 65, 11, 21, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# 65 -> 1 -> 35 -> 4 -> 3 -> 6 -> 7 -> 8 -> 11 -> 21 -> 22 -> 23 ->
print(intersection(linked_list_5, linked_list_6))
# 65 -> 7 ->


# Edge Cases:
# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [1, 7, 8]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))
# 8 -> 1 -> 7 ->
print(intersection(linked_list_7, linked_list_8))
#

# Test case 5
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))
#
print(intersection(linked_list_9, linked_list_10))
#

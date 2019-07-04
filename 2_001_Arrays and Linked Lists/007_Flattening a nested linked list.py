#%% Imports and function declaration
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    def flatten_deep(self):
        value_list = []
        node = self.head

        while node.next is not None:
            value_list.append(node.value)
            node = node.next
        value_list.append(node.value)
        return value_list


class NestedLinkedList(LinkedList):
    def flatten(self):
        values = []
        for element in self.flatten_deep():
            values.append(element.flatten_deep())
        values = [item for sublist in values for item in sublist]
        values.sort()
        return values

#%% First Challenge - Definition
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)

#%% First Challenge - Solution
solution = nested_linked_list.flatten()
assert solution == [1, 2, 3, 4, 5]

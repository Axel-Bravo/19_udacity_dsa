class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            self.head = Node(value)
        else:
            previous_head = self.head
            self.head = Node(value)
            self.head.next = previous_head

    def append(self, value):
        """ Append a value to the end of the list. """
        position_tail = self.head

        if position_tail is None:
            self.head = Node(value)

        else:
            while position_tail.next:  # Moving to the end of the list
                position_tail = position_tail.next

            position_tail.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        position_tail = self.head

        while position_tail.next:  # Moving to the end of the list
            if position_tail.value == value:
                return position_tail
            position_tail = position_tail.next

        return None

    def remove(self, value):
        """ Remove first occurrence of value. """
        position_prev_tail = None
        position_tail = self.head

        while position_tail:  # Moving to the end of the list
            if position_tail.value == value:
                if position_prev_tail is None:
                    self.head = position_tail.next
                    break
                else:
                    position_prev_tail.next = position_tail.next
                    break

            position_prev_tail = position_tail
            position_tail = position_tail.next

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        first_node = self.head.value
        self.head = self.head.next
        return first_node

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        position_tail_continuity = None
        position_tail = self.head

        if pos == 0:
            position_tail_continuity = self.head
            self.head = Node(value)
            self.head.next = position_tail_continuity
            return

        else:
            for _ in range(1, pos - 1):  # Moving to the previous, to insertion, position

                if position_tail.next is None:  # Selected position out of "linked list" bounds
                    position_tail.next = Node(value)
                    return

                position_tail = position_tail.next

            position_tail_continuity = position_tail.next
            position_tail.next = Node(value)
            position_tail = position_tail.next
            position_tail.next = position_tail_continuity

            return

    def size(self):
        """ Return the size or length of the linked list. """
        position_tail = self.head
        length = 0

        while position_tail is not None:
            position_tail = position_tail.next
            length += 1

        return length

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


if __name__ == '__main__':
    # Test prepend
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    linked_list.prepend(2)
    assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

    # Test append
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

    # Test search
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

    # Test remove
    linked_list.remove(1)
    assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

    # Test pop
    value = linked_list.pop()
    assert value == 2, f"list contents: {linked_list.to_list()}"
    assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

    # Test insert
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

    # Test size
    assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"



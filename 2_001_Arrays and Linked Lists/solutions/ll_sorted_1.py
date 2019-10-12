# Solution

class SortedLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        if self.head is None:
            self.head = Node(value)
            return
        
        if value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return
        
        node = self.head
        while node.next is not None and value >= node.next.value:
            node = node.next
            
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        
        return None

# Test cases
linked_list = SortedLinkedList()
linked_list.append(3)
print ("Pass" if (linked_list.head.value == 3) else "Fail")

linked_list.append(2)
print ("Pass" if (linked_list.head.value == 2) else "Fail")

linked_list.append(4)
node = linked_list.head.next.next
print ("Pass" if (node.value == 4) else "Fail")

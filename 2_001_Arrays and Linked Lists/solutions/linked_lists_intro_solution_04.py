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
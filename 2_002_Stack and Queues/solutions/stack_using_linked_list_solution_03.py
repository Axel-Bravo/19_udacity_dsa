class Stack:
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self, value):
        new_node = Node(value)        
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head    # place the new node at the head of the linked list (top)
            self.head = new_node

        self.num_elements += 1
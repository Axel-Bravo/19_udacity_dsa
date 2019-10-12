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
            new_node.next = self.head # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1
        
    def pop(self):
        if self.is_empty():
            return
        
        value = self.head.value # copy data to a local variable
        self.head = self.head.next # move head pointer to point to next node (top is removed by doing so)
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
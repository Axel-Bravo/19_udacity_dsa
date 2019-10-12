class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
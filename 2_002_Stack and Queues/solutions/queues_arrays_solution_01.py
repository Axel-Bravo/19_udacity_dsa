class Queue:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0
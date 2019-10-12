def reverse_queue(queue):
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())

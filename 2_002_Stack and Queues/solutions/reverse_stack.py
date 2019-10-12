def reverse_stack(stack):
    holder_stack = Stack()
    while not stack.is_empty():
        popped_element = stack.pop()
        holder_stack.push(popped_element)
    _reverse_stack_recursion(stack, holder_stack)


def _reverse_stack_recursion(stack, holder_stack):
    if holder_stack.is_empty():
        return
    popped_element = holder_stack.pop()
    _reverse_stack_recursion(stack, holder_stack)
    stack.push(popped_element)

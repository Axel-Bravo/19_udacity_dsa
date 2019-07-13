#%% Imports and function declaration
class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    stack = Stack()

    for element in input_list:
        if element in ['+', '-', '*', '/']:
            element_2 = stack.pop()
            element_1 = stack.pop()
            stack.push(str(int(eval(element_1 + element + element_2))))

        else:
            stack.push(element)

    return stack.pop()


#%% Testing Zone


# Case 1
test_case_1 = [["3", "1", "+", "4", "*"], 16]
print('Case 1 is: {}'.format(evaluate_post_fix(test_case_1[0])))

# Case 2
test_case_2 = [["4", "13", "5", "/", "+"], 6]
print('Case 2 is: {}'.format(evaluate_post_fix(test_case_2[0])))


# Case 3
test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
print('Case 3 is: {}'.format(evaluate_post_fix(test_case_3[0])))



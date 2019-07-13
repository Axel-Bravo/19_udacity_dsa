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


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of bracket reversals needed
    """

    # Correcting extreme cases
    extra_movements = 0

    if input_string[0] == '}':
        input_string = '{' + input_string[1:]
        extra_movements += 1
    if input_string[len(input_string)-1] == '{':
        input_string = input_string[:len(input_string)-1] + '}'
        extra_movements += 1

    prev_char = '-'

    # Cases that match
    if len(input_string) % 2 != 0:  # Non even length cases can never be balanced
        return -1

    else:
        stack = Stack()

        for char in input_string:
            if prev_char+char == '{}':
                _ = stack.pop()
                prev_char = stack.top()

                if stack.size() == 0:
                    prev_char = '-'
            else:
                stack.push(char)
                prev_char = char

    return int(stack.size()/2) + extra_movements


#%% Testing

# Case 1
test_case_1 = ["}}}}", 2]
print('Case 1 is :{}'.format(minimum_bracket_reversals(test_case_1[0])))

# Case 2
test_case_2 = ["}}{{", 2]
print('Case 2 is :{}'.format(minimum_bracket_reversals(test_case_2[0])))


# Case 3
test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
print('Case 3 is :{}'.format(minimum_bracket_reversals(test_case_3[0])))


# Case 4
test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
print('Case 4 is :{}'.format(minimum_bracket_reversals(test_case_4[0])))

# Case 5
test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
print('Case 5 is :{}'.format(minimum_bracket_reversals(test_case_5[0])))


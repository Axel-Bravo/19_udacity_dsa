def minimum_bracket_reversals(input_string):
    if len(input_string) % 2 == 1:
        return -1

    stack = Stack()
    count = 0
    for bracket in input_string:
        if stack.is_empty():
            stack.push(bracket)
        else:
            top = stack.top()
            if top != bracket:
                if top == '{':
                    stack.pop()
                    continue
            stack.push(bracket)

    ls = list()
    while not stack.is_empty():
        first = stack.pop()
        second = stack.pop()
        ls.append(first)
        ls.append(second)
        if first == '}' and second == '}':
            count += 1
        elif first == '{' and second == '}':
            count += 2
        elif first == '{' and second == '{':
            count += 1
    return count

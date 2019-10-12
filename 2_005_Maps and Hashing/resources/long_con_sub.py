def longest_consecutive_subsequence(input_list):
    element_dict = dict()

    for index, element in enumerate(input_list):
        element_dict[element] = index

    max_length = -1
    starts_at = len(input_list)

    for index, element in enumerate(input_list):
        current_starts = index
        element_dict[element] = -1

        current_count = 1

        # check upwards
        current = element + 1

        while current in element_dict and element_dict[current] > 0:
            current_count += 1
            element_dict[current] = -1
            current = current + 1

        # check downwards
        current = element - 1
        while current in element_dict and element_dict[current] > 0:
            current_starts = element_dict[current]
            current_count += 1
            element_dict[current] = -1
            current = current - 1

        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts
            max_length = current_count

    start_element = input_list[starts_at]
    return [element for element in range(start_element, start_element + max_length)]




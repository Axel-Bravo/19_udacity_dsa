#%% Imports and function declaration


def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list

    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """

    lower_case_char = []
    upper_case_char = []

    for char in string:
        if ord(char) < 91:  # 90 is Z
            upper_case_char.append(char)
        else:
            lower_case_char.append(char)


    lower_case_char = mergesort(lower_case_char)
    upper_case_char = mergesort(upper_case_char)


    result = ''

    for char in string:
        if ord(char) < 91:  # 90 is Z
            result += upper_case_char.pop(0)
        else:
            result += lower_case_char.pop(0)

    return result


#%% Test official
test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
assert case_sort(test_string) == solution, "Error, something went wrong"

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
assert case_sort(test_string) == solution, "Error, something went wrong"
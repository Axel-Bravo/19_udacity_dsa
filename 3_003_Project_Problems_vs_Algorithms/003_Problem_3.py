#%% Imports and functions declarations
def rearrange_digits(input_list: list, first_layer: bool = False) -> list:
    """
        Rearrange Array Elements so as to form two number such that their sum is maximum.

        Args:
           input_list(list): Input List
           first_layer(bool): placeholder to know if we are in the first layer of the recursion (special case)
        Returns:
           (int),(int): Two maximum sums
        """

    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = rearrange_digits(left)
    right = rearrange_digits(right)

    return merge(left, right, first_layer)


def merge(left: list, right: list, first_layer: bool = False) -> list:
    merged = []
    left_index = 0
    right_index = 0

    if first_layer:  # Special case for the last merging step
        num_max_left = ''
        num_max_right = ''
        num_to_left = True

        # Alternating between left and right indexes
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                if num_to_left:
                    num_max_left = str(right[right_index]) + num_max_left
                else:
                    num_max_right = str(right[right_index]) + num_max_right
                right_index += 1
            else:
                if num_to_left:
                    num_max_left = str(left[left_index]) + num_max_left
                else:
                    num_max_right = str(left[left_index]) + num_max_right
                left_index += 1

            num_to_left = not num_to_left  # Distribute the numbers on each of the list

        # Exhausting remaining index
        while left_index < len(left):   # left index is not exhausted
            if num_to_left:
                num_max_left = str(left[left_index]) + num_max_left
            else:
                num_max_right = str(left[left_index]) + num_max_right

            left_index += 1
            num_to_left = not num_to_left

        while right_index < len(right):  # right index is not exhausted
            if num_to_left:
                num_max_left = str(right[right_index]) + num_max_left
            else:
                num_max_right = str(right[right_index]) + num_max_right

            right_index += 1
            num_to_left = not num_to_left

        return [int(num_max_left), int(num_max_right)]

    else:  # Normal merging case
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


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


#%% Testing - Official
# Normal cases
print('Normal Cases:')
print('Test 1:')
list_num = [1, 2, 3, 4, 5]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [531, 42]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 2:')
list_num = [4, 6, 2, 5, 9, 8]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [852, 964]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 3:')
list_num = [1, 2, 3]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [31, 2]:
    print('Pass \n')
else:
    print("Fail \n")

# Edge cases
print('Edge Cases:')
print('Test 4:')
list_num = [1, 1, 1]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [11, 1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 5:')
list_num = [1]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 6:')
list_num = []
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == []:
    print('Pass \n')
else:
    print("Fail \n")
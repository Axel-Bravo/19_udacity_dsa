#%% Imports and functions declaration
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    i = 0
    i_null = 0
    i_two = len(input_list) - 1

    while i <= i_two:
        if input_list[i] == 0:
            input_list[i] = input_list[i_null]
            input_list[i_null] = 0
            i_null += 1
            i += 1

        elif input_list[i] == 2:
            temp_val = input_list[i_two]
            input_list[i_two] = 2
            input_list[i] = temp_val
            i_two -= 1

        else:
            i += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

#%% Testing - Official
# Normal cases
print('Normal Cases:')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('\n')

# Edge cases
print('Edge Cases:')
test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])

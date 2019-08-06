#%% Imports and functions declarations
import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return None

    max_val = - float("inf")
    min_val = float("inf")

    for int in ints:
        if int > max_val:
            max_val = int
        if int < min_val:
            min_val = int

    return (min_val, max_val)

#%% Testing - Official
# Normal cases
print('Normal Cases:')
# Case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Case 2
l = [i for i in range(-12, 25)]  # a list containing -12 - 24
random.shuffle(l)
print("Pass" if ((-12, 24) == get_min_max(l)) else "Fail")
print('\n')

# Edge cases
print('Edge Cases:')
# Case 3
l = [i for i in range(300, 301)]  # a list containing 300
random.shuffle(l)
print("Pass" if ((300, 300) == get_min_max(l)) else "Fail")

# Case 4
l = []  # an empty list
print("Pass" if (None == get_min_max(l)) else "Fail")

# Case 5
l = [i for i in range(-24, -1)]  # a list containing -24 - -2
random.shuffle(l)
print("Pass" if ((-24, -2) == get_min_max(l)) else "Fail")

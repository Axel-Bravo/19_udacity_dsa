#%% Imports and functions declaration
def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        return None

    if (number == 0) or (number == 1):
        return number

    i_start = 0
    i_end = number // 2

    while i_start <= i_end:
        i_middle = (i_end + i_start) // 2
        i_middle_pow = i_middle * i_middle

        if i_middle_pow == number:
            return i_middle
        elif i_middle_pow < number:
            i_start = i_middle + 1
            result = i_middle
        else:
            i_end = i_middle - 1

    return result

#%% Testing - Official
# Normal cases
print('Normal Cases:')
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass \n" if (5 == sqrt(27)) else "Fail \n")

# Edge cases
print('Edge Cases:')
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (99380 == sqrt(9876543210)) else "Fail")

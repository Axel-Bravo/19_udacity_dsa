#%% Imports and functions declaration


def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    num_div = 1

    while True:
        if number == 0:
            return 0
        elif (number // num_div) == num_div:
            return num_div
        else:
            num_div += 1


#%% Testing - Official
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

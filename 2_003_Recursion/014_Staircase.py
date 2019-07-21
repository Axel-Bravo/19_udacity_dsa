#%% Import and function declaration


def staircase(n):
    """
    :param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        climb_ways = 0
        climb_ways += staircase(n - 1)
        climb_ways += staircase(n - 2)
        climb_ways += staircase(n - 3)

        return climb_ways


#%% Testing
n = 3
solution = 4
print(staircase(n))

n = 4
solution = 7
print(staircase(n))

n = 7
solution = 44
print(staircase(n))
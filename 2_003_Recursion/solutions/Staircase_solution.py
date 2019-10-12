# Solution
## Read input as specified in the question.
## Print output as specified in the question.


def staircase(n):
    if n <= 0:
        return 1
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
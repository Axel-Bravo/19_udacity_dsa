#%% Imports and functions declaration
def min_operations(target: int) -> int:
    """
    Return number of steps taken to reach a target number
    input: target number (as an integer)
    output: number of steps (as an integer)
    """

    steps = 0

    while target != 0:
        while (target / 2) == (target // 2):
            target = target // 2
            steps += 1

        target -= 1
        steps += 1

    return steps

#%% Testing - Official
target = 18
solution = 6
assert min_operations(target=target) == solution, 'Not working properly'

target = 69
solution = 9
assert min_operations(target=target) == solution, 'Not working properly'

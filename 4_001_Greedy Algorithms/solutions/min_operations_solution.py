def min_operations(target):
    """
    Return number of steps taken to reach a target number
    input:- target number an integer
    output:- number of steps an integer
    """
    num_steps = 0
    
    # start backwards from the target
    # if target is odd --> subtract 1
    # if target is even --> divide by 2
    while target != 0:
        if target % 2 == 0:
            target = target // 2

        else:
            target = target - 1
        num_steps += 1
    return num_steps
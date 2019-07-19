#%% Import and function declaration
# Code

import copy


def permute(l):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      l(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item being represented by a list
    """

    if len(l) <= 1:
        return [l]

    elif len(l) == 2:
        return [l, l[::-1]]

    else:
        output = []
        current_level = l[0]
        prev_level = permute(l[1:])

        for element in prev_level:  # For each answer from previous level
            for pos in range(len(element) + 1):  # For each possible position to put this level value
                temp_list = []
                temp_element = element.copy()
                for i in range(len(element) + 1):
                    if pos == i:
                        temp_list.append(current_level)
                    else:
                        temp_list.append(temp_element.pop())
                output.append(temp_list)
        return output

#%% Testing


permute([0, 1, 2])
#  Expected resutls [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]))


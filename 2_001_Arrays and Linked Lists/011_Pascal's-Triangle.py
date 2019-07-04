#%% Imports and functions declarations
from math import factorial


def combinations(total_num: int, choosen_num: int) -> int:
    """
    Returns the number of available combinations given a number of elements and the subspace selected
    :param total_num: number of total elements
    :param choosen_num: number of elements of the subspace
    :return: number of total combinations
    """
    return int(factorial(total_num)/(factorial(choosen_num)*factorial(total_num-choosen_num)))


def nth_row_pascal(num_row: int) -> list:
    """
    Given the number of the row, generates the specifiy values present in this pascal triangle
    :param num_row: number of row to represent
    :return: pascal's triangle row
    """
    row_result = []
    for i in range(num_row+1):
        row_result.append(combinations(num_row, i))
    return row_result

#%%

nth_row_pascal(5)

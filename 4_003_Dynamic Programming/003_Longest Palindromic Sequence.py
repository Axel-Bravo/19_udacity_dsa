#%% Imports and functions declarations
def matrix_constructor(string_col: str, string_row: str) -> list:
    """
    Construct a matrix suited for lcs
    :param string_col: string occupying the columns position
    :param string_row: string occupying the rows position
    :return: matrix on the proper format
    """

    string_col = '0' + string_col
    string_row = '0' + string_row
    matrix = []

    for i_row, row in enumerate(string_row):
        row_list = []
        for i_col, col in enumerate(string_col):
            if i_row == 0:  # Naming column
                row_list.append(col)
            else:
                if i_col == 0:  # Naming row
                    row_list.append(row)
                elif i_col == i_row:
                    row_list.append(1)
                else:
                    row_list.append(0)

        matrix.append(row_list)

    return matrix


def lps(input_string: str) -> int:
    """
    Given a string, returns the maximum palindrome lenght
    :param input_string: string to find palindromes on
    :return: maximum palindrom length
    """
    matrix = matrix_constructor(string_col=input_string, string_row=input_string)

    for i_row in range(len(matrix)-2, 0, -1):
        for i_col in range(i_row+1, len(matrix)):
            if matrix[i_row][0] == matrix[0][i_col]:  # Match - Equals to the bottom-left of that cell plus two.
                bottom_left_cell = matrix[i_row+1][i_col-1]
                matrix[i_row][i_col] = bottom_left_cell + 2
            else:  # Non Match - Maximum value from either directly to the left or the bottom cell.
                left_cell = matrix[i_row][i_col-1]
                bottom_cell = matrix[i_row+1][i_col]
                matrix[i_row][i_col] = max(left_cell, bottom_cell)

    return matrix[1][len(matrix)-1]


#%% Test - Dev
string = 'TACOCAT'
solution = 7
assert solution == lps(input_string=string), 'Error on the algorithm implementation'

string = 'BANANA'
solution = 5
assert solution == lps(input_string=string), 'Error on the algorithm implementation'

string = 'BANANO'
solution = 3
assert solution == lps(input_string=string), 'Error on the algorithm implementation'

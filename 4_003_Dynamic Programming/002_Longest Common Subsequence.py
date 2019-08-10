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
                else:
                    row_list.append(0)

        matrix.append(row_list)

    return matrix


def lcs(string_a: str, string_b: str) -> int:
    """
    Performs an unnormalized "longest common sequence" analysis of two strings
    :param string_a: a string
    :param string_b: another string
    :return: the length of the longest common sequence
    """
    matrix = matrix_constructor(string_col=string_a, string_row=string_b)
    max_lcs = 0

    for i_row in range(1, len(matrix)):
        row_value = matrix[i_row][0]  # value to compare all row's values

        for i_col in range(1, len(matrix[0])):
            col_value = matrix[0][i_col]  # value to compare all columns' values

            if row_value == col_value:  # Match: diagonal value + 1
                if (i_row == 1) or (i_col == 1):
                    diag_cell = 0
                else:
                    diag_cell = matrix[i_row-1][i_col-1]

                cell_value = diag_cell + 1
                matrix[i_row][i_col] = cell_value
                max_lcs = max(max_lcs, cell_value)

            else:  # No match: max of top/left cells
                if i_col == 1:
                    left_cell = 0
                else:
                    left_cell = matrix[i_row][i_col-1]

                if i_row == 1:
                    top_cell = 0
                else:
                    top_cell = matrix[i_row-1][i_col]

                cell_value = max(left_cell, top_cell)
                matrix[i_row][i_col] = cell_value
                max_lcs = max(max_lcs, cell_value)

    return max_lcs


#%% Testing
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"
solution = 5
assert solution == lcs(string_a=test_A1, string_b=test_B1), "Error, problem not properly solved"

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"
solution = 7
assert solution == lcs(string_a=test_A2, string_b=test_B2), "Error, problem not properly solved"
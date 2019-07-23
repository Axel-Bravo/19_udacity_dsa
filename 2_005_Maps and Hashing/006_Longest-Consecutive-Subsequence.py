#%% Imports and function declaration


def longest_consecutive_subsequence(input_list):

    # iterate over the list and store element in input_list suitable data structure

    # traverse / go over the data structure in input_list reasonable order to determine the solution

    input_list.sort()
    input_list = [element for element in set(input_list)]
    input_list_subst = []

    for i, value in enumerate(input_list):
        if  (i != (len(input_list)-1)):
            if i >= 1:
                if (input_list_subst[i-1] == -1) & (input_list[i] - input_list[i + 1] != -1):
                    input_list_subst.append(-1)

            input_list_subst.append(input_list[i] - input_list[i + 1])


        else:
            pass

    i_stored = 0
    i_stored_max = 0
    i_stored_length = 0
    i_stored_max_length = 0
    unbroken_consecutive = True

    for i, value in enumerate(input_list_subst):
        if value == -1:
            i_stored_length += 1

            if i_stored != 0:
                pass
            else:
                i_stored = i
        else:
            unbroken_consecutive = False

            if i_stored is not 0:
                if i_stored_length > i_stored_max_length:
                    i_stored_max_length = i_stored_length
                    i_stored_max = i_stored

                i_stored = 0
                i_stored_length = 0

    if unbroken_consecutive:
        return input_list
    else:
        return input_list[i_stored_max-1: i_stored_max + i_stored_max_length-1]


#%% Testing

test_case = [5, 4, 7, 10, 1, 3, 55, 2]
sol = [1, 2, 3, 4, 5]
print(longest_consecutive_subsequence(test_case))

test_case = [2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ]
sol = [8, 9, 10, 11, 12]
print(longest_consecutive_subsequence(test_case))

test_case = [0, 1, 2, 3, 4]
sol = [0, 1, 2, 3, 4]
print(longest_consecutive_subsequence(test_case))
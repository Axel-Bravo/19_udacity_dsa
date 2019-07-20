#%% Import and function declaration
def deep_reverse(arr):
    if type(arr) is not list:
        return arr
    else:
        results = []
        arr = arr[::-1]
        for element in arr:
            results.append(deep_reverse(element))
        return results


#%% Testing
arr_1 = [1, 2, 3, 4, 5]
solution_1 = [5, 4, 3, 2, 1]

arr_2 = [1, 2, [3, 4, 5], 4, 5]
solution_2 = [5, 4, [5, 4, 3], 2, 1]

arr_3 = [1, [2, 3, [4, [5, 6]]]]
solution_3 = [[[[6, 5], 4], 3, 2], 1]
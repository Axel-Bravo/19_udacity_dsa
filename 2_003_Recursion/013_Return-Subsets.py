#%% Imports and function declaration

def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    """

    if len(arr) <= 1:
        return [arr]

    else:
        results = list()
        results.append(arr)

        for i_pos in range(len(arr)):
            temp_arr = arr.copy()
            temp_arr.pop(i_pos)
            results.extend(subsets(temp_arr))

        results_mod = []
        for i, item in enumerate(results):
            if i == results.index(item):  # Case detected is the one we are
                results_mod.append(item)
            else:
                pass
        return results_mod


#%% Testing
"""
arr = [9]
solution = [[], [9]]
print(subsets(arr))

arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
print(subsets(arr))
"""

#%%
arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]
print(subsets(arr))

solution = [     ]

sol_given = [ [15],  [12], [9]]  # ME sobra uno de cada tipo :S



#%%

arr = [9, 8, 9, 8]
print(subsets(arr))

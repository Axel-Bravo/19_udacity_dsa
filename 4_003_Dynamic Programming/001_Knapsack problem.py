#%% Imports and functions declarations
import collections
Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight: int, items: list) -> int:
    """
    Get the maximum value of the knapsack.
    """
    items = sorted(items, key=lambda x: x.weight)
    knapsack = [0 for _ in range(knapsack_max_weight + 1)]

    for item in items:  # Process each one of the items
        first_item_usage_pos = None

        for i_knapsack in range(item.weight, len(knapsack)):  # Try to fit it in the "knapsack table"
            if item.value > knapsack[i_knapsack]:
                knapsack[i_knapsack] = item.value

                if not first_item_usage_pos:
                    first_item_usage_pos = i_knapsack

            if i_knapsack - item.weight > 0:
                if first_item_usage_pos:
                    if i_knapsack < first_item_usage_pos + item.weight:  # Value not used twice
                        complement_val = knapsack[i_knapsack - item.weight]

                        if item.value + complement_val > knapsack[i_knapsack]:
                            knapsack[i_knapsack] = item.value + complement_val
                    else:  # Can not use value twice
                        pass
                else:  # Value never used
                    complement_val = knapsack[i_knapsack - item.weight]

                    if item.value + complement_val > knapsack[i_knapsack]:
                        knapsack[i_knapsack] = item.value + complement_val

                        if not first_item_usage_pos:
                            first_item_usage_pos = i_knapsack

    return knapsack[knapsack_max_weight]

#%% Dev Zone


knapsack_max_weight = 15
items = [Item(10, 7), Item(9, 8), Item(5, 6)]
print(max_value(knapsack_max_weight, items))


knapsack_max_weight = 25
items = [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]
print(max_value(knapsack_max_weight, items))


#%%
tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == max_value(**test['input'])



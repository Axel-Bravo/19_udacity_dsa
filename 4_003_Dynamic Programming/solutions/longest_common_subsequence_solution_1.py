def lcs(string_a, string_b):
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]

    for char_a_i, char_a in enumerate(string_a):
        for char_b_i, char_b in enumerate(string_b):
            if char_a == char_b:
                lookup_table[char_a_i + 1][char_b_i + 1] = lookup_table[char_a_i][char_b_i] + 1
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i])

    return lookup_table[-1][-1]
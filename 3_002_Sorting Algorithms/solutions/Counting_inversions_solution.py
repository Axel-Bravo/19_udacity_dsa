def count_inversions(arr):
    start_index = 0
    end_index = len(arr) - 1
    output = inversion_count_func(arr, start_index, end_index)
    return output


def inversion_count_func(arr, start_index, end_index):
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2
    
    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start_index, mid_index)
    
    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid_index + 1, end_index)

    output = left_answer + right_answer
    
    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            count = count + (end_one - left_index + 1)           # left > right hence it's an inversion
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1

        if left_index > end_one:
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count
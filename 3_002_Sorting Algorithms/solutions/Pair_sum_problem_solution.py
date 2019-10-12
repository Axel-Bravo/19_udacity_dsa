def pair_sum(arr, target):
    # sort the list
    arr.sort()
    
    # initialize two pointer - one from start of the array and other from the end
    front_index = 0
    back_index = len(arr) - 1

    # shift the pointers
    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]

        if front + back == target:
            return [front, back]
        elif front + back < target:       # sum < target ==> shift front pointer forward
            front_index += 1 
        else:
            back_index -= 1               # sum > target ==> shift back pointer backward

    return [None, None]
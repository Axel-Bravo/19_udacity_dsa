#%% Imports and functions declaration


def bubble_sort_1(list):
    for _ in range(len(list)):
        for i_pos in range(len(list)-1):
            therm_left = list[i_pos]
            therm_right = list[i_pos+1]

            if therm_left > therm_right:
                list[i_pos] = therm_right
                list[i_pos+1] = therm_left
            else:
                pass

    return list


def is_time_bigger(time, time_to_compare):

    t_hours, t_min = time
    ttc_hours, ttc_min = time_to_compare

    if t_hours > ttc_hours:
        return True
    elif t_hours < ttc_hours:
        return False
    else:

        if t_min >= ttc_min:
            return True
        else:
            return False


def bubble_sort_2(list):

    for _ in range(len(list)):
        for i_pos in range(len(list)-1):
            time_left = list[i_pos]
            time_right = list[i_pos+1]

            if is_time_bigger(time=time_left, time_to_compare=time_right):
                pass
            else:
                list[i_pos] = time_right
                list[i_pos + 1] = time_left

    return list


#%% Test Official
# Test Bubblesort 1
wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")

# Test Bubblesort 2
# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]
bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")
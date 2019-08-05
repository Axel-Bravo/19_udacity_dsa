#%% Imports and functions declaration
def min_platforms(arrival: int, departure:int) -> int:
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    so that no train has to wait for other(s) to leave
    """

    num_platforms = 0

    for time in range(min(arrival), max(departure) + 10, 10):
        temp_num_platforms = 0

        for i_train in range(len(arrival)):
            if (time >= arrival[i_train]) and (time < departure[i_train]):
                temp_num_platforms +=1

        if temp_num_platforms > num_platforms:
            num_platforms = temp_num_platforms

    return num_platforms


#%% Testing - Official
arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
assert min_platforms(arrival=arrival, departure=departure) == 3, 'Not properly working'

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
assert min_platforms(arrival=arrival, departure=departure) == 2, 'Not properly working'

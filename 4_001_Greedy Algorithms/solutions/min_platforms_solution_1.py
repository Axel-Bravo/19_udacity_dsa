def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()

    platform_count = 1
    output = 1
    i = 1
    j = 0

    while i < len(arrival) and j < len(arrival):

        if arrival[i] < departure[j]:
            platform_count += 1
            i += 1

            if platform_count > output:
                output = platform_count
        else:
            platform_count -= 1
            j += 1

    return output
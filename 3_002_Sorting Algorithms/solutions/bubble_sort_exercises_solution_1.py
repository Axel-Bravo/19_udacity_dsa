def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index] = prev
            l[index - 1] = this
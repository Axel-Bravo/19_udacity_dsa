def print_integers(n):
    if n <= 0:
        return
    print(n)
    print_integers(n - 1)
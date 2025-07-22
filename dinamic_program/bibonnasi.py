def fibona(n):
    if n == 1 or n == 0:
        return 1
    return n * fibona(n-1)


print(fibona(6))


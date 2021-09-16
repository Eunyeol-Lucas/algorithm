def recursion(n):
    result = 1
    if n > 0:
        result = n*recursion(n-1)
    return result

print(recursion(int(input())))
def construct(n):
    n = n + sum(map(int, str(n)))
    return n

n_list = [0]*10001

for i in range(1, 10001):
    n_list[i] = construct(i)

for i in range(1, 10001):
    if i not in n_list:
        print(i)

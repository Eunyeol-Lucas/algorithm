n = int(input())
check = [0] * (n + 1)
dict = {1: []}
i = 1
while i**2 <= n:
    check[i**2] = 1
    dict[1].append(i**2)
    i += 1

j = 1
tmp = dict.get(j)
while True:
    if n in tmp:
        break
    tmp2 = []
    for t in tmp:
        for t2 in dict.get(1):
            if t + t2 <= n and not check[t + t2]:
                check[t + t2] = 1
                tmp2.append(t+t2)

    j += 1
    dict[j] = tmp2
    tmp = tmp2

print(j)

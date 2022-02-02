N, M = map(int, input().split())
list = []
out = []
while True:
    A, B = map(str, input().split())
    if (A and B) == '0':
        break
    A = int(A)
    if A <= N:
        if out.count(A) < M:
            out.append(A)
            list.append((A, B))

list = sorted(sorted(list), key = lambda x : ((x[0] % 2 == 0, x[0]), len(x[1])))

for a, b in list:
    print(a, b)
N = int(input())
result = 0
for i in range(N+1):
    A = list(map(int, str(i)))
    result = i + sum(A)
    if N == result:
        print(i)
        break
    if i == N:
        print(0)
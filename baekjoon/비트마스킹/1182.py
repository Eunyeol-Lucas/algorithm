from sys import stdin
input = stdin.readline


N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

for i in range(1, 1 << N):
    tmp = 0
    for j in range(N):
        k = (i << j)
        if i & k:
            tmp += arr[j]
    if tmp == S:
        answer += 1
print(answer)


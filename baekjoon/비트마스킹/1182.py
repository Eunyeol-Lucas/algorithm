from sys import stdin
input = stdin.readline

N, S = 5, 0
arr = [-7, -3, -2, 5, 8]


# N, S = map(int, input().split())
# arr = list(map(int, input().split()))

answer = 0

for i in range(1, 1 << N):
    tmp = 0
    for j in range(N):
        print(bin(i), bin(1 << j))
        if i & (1 << j):
            tmp += arr[j]
    if tmp == S:
        answer += 1
print(answer)


print(11 & 22)
print(11 | 22)
print(11 ^ 22)

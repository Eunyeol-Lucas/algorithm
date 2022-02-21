import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0]

idx = 1
for i in range(N):
    tmp = arr[i]
    if tmp < dp[-1]:
        dp.append(tmp)
        idx += 1
    for j in range(idx):
        if tmp >= dp[j]:
            dp[j] = tmp
            break

print(idx)

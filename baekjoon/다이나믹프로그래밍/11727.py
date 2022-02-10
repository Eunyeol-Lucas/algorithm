N = int(input())

# 1, 3, 5, 11
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
for i in range(3, 1001):
    dp[i] = dp[i-2] * 2 + dp[i-1]
print(dp[N] % 10007)

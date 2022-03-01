N = int(input())

dp = [0] * (N+1)
if N >= 2:
    dp[2] = 3
    # dp[4] = dp[4-2] * 3 + dp[4-4] * 3 + 2
    # dp[6] = dp[6-2] * 3 + dp[6-4] * 3 + dp[6-6] * 3 + 2
    # dp[8] = dp[8-2] * 3 + dp[8-4] * 3 + dp[8-6] * 3  + dp[8-8] * 3 + 2
    for i in range(4, N+1):
        if i % 2 == 0:
            dp[i] += (dp[i-2] * 3 + 2)
            for j in range(i - 4, -1, -2):
                dp[i] += dp[j] * 2
print(dp[N])

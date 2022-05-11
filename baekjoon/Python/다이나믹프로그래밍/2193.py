import sys

n = int(sys.stdin.readline())

dp = [[0, 0] for _ in range(91)]

dp[1] = [0, 1]
dp[2] = [1, 0]
# i 자리 이진수가 0으로 끝나는 경우는 i - 1 자리의 0과 1로 끝나는 수의 합이고
# i 자리 이진수가 1로 끝나는 경우는 i - 1자리가 0으로 끝나는 경우
for i in range(3, 91):
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = dp[i-1][0]


print(sum(dp[n]))

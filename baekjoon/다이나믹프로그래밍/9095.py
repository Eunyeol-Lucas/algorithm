import sys

input = sys.stdin.readline
T = int(input())
dp = [0] * 11
# 1부터 3까지는 규칙이 없음
dp[1], dp[2], dp[3] = 1, 2, 4

# 4 이상부터 4의 경우 첫 번째, 두 번째, 세번째 경우의 수의 합
# 5의 경우 두 번째, 세 번째, 네 번째 경우의 수의 합
# 을이용하여 점화식을 구함
for _ in range(T):
    N = int(input())
    for i in range(4, N + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[N])

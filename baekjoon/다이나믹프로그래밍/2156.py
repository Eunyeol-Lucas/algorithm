import sys
input = sys.stdin.readline

N = int(input())

arr = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

# 1잔이 있을 때, 최대값은 1잔을 마셨을 때
dp[1] = arr[1]
if N > 1:
    # 2잔이 있을 때, 최대값을 두 잔을 모두 마셨을 경우
    dp[2] = arr[1] + arr[2]

    # 최대 연속해서 두 잔까지 마실 수 있다.
    # 4잔의 경우, 
        # 1. 4번째 잔을 마시 지 않고 3번째 잔까지 마셨을 때의 최대값, 
        # 2. 첫 잔과, 3번째, 4번째 까지 마신 양, 
        # 3. 2번째 잔까지 마시고 4번째 잔을 마셨을 때 
    # 3 경우 중 가장 많이 마실 수 있는 양을 선택한다.
    # 3잔 이상의 N잔의 경우, N-1잔까지 최대값, N-3잔까지 최대값 + N-1잔의 양 + N잔의 양, N-2잔 까지 최대값 + N 잔의 양 중 최대값이다.
    for i in range(3, N+1):
        dp[i] = max(dp[i-1], dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

print(dp[N])

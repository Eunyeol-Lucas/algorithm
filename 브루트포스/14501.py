import sys

input = sys.stdin.readline

n = int(input())
_list = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]
for i in range(n-1, -1, -1):
    if i + _list[i][0] > n:        
        dp[i] = dp[i+1]
    else:
        dp[i] = max(_list[i][1] + dp[i + _list[i][0]], dp[i+1])
        
print(dp[0])
import sys

input = sys.stdin.readline
n = int(input())
num = [int(input()) for _ in range(n)]
N = 1000001
mod = 1000000009
dp = [0] * N
# 1, 2, 3의 조합으로 숫자 만들기
# 1을 만들 수 있는 숫자 조합은 1 하나로, 1 가지
# 2를 만들 수 있는 숫자 조합:  (1,1) (2) , 2가지
# 3을 만들 수 있는 숫자 조합: (1,1,1) (1,2) (2,1) (3), 4가지 
# 4를 만들 수 있는 숫자 조합: (1,1,1,1) (1,2,1) (1,1,2) (1,3) (2,1,1) (2,2) (3), 7가지
# 4 이상의 수 i는 i -1, i-2 , i-3의 숫자에 각각 1, 2, 3을 더한 숫자로 각 조합의 합을 구하면 됨.
dp[1] = 1
dp[2] = 2
dp[3] = 4


for i in range(4, N):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % mod

for i in num:
    print(dp[i] % mod)

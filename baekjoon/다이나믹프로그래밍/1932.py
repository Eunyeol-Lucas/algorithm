import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i+1):
        # i 번째 층의 0번 인덱스는 i-1층의 0번 인덱스만 가능
        if j == 0:
            dp[i][j] += dp[i-1][j]
        # i 번쨰 층의 마지막 인덱스는 i-1층의 마지막 인덱스에서만 접근 가능
        elif i == j:
            dp[i][j] += dp[i-1][j-1]
        # 처음과 마지막을 제외한 것들은 직전의 같은 인덱스 또는 -1 인덱스에서 온 값을 더함.
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j]) 


print(max(dp[-1]))

'''
5
1
0 1
8 1 7
2 7 0 1
4 5 2 6 44
'''

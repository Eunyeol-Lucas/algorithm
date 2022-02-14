import sys

n, k = map(int, sys.stdin.readline().split())
# n과 k가 1부터 200까지일때 경우의 모두 담을 배열을 선언(메모이제이션)
dp = [[0] * 201 for _ in range(201)]

# n과 상관없이 k가 1일 경우, n을 만들 수 있는 수는 n 자신 1개
# k가 2일 경우, n을 만들 수 있는 수는 n + 1
# n = 2, k = 2 => (0,2) (2,0) (3,0) / n = 5, k => (0,5) (5,0) (1,4) (4,1) (2,3) (3,2)
# n 이 1일 경우 k가 n을 만들 수 있는 수는 k개

for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i + 1
    dp[i][1] = i

# k가 2일 떄, n이 각 각 1, 2, 3, 4, 5일 경우
# 2, 3, 4, 5, 6
# k가 3일 때,
# 3, 6, 10, 15, 21
# 점화식 dp[i][j] = dp[i-1][j] + dp[i][j-1]
for i in range(2, 201):
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[k][n])


# 시간초과
'''
a, b = list(map(int, sys.stdin.readline().split()))
arr = [0] * b
answer = 0


def DFS(L):
    global answer
    if L == b:
        if sum(arr) == a:
            answer += 1
    else:
        for i in range(0, a+1):
            arr[L] = i
            DFS(L+1)


DFS(0)
print(answer)
'''

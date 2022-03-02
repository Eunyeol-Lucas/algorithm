import sys

input = sys.stdin.readline

N = int(input())

arr = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N+1)]

answer = 1000 * N

# 첫번째 집의 색과 N번째 집의 색이 달라야 하기 때문에
# 첫번째 집의 색을 지정한 뒤 ,N 번째 집의 색이 첫번째 집의 색이 아닐 떄 최소값을 찾는 방법을 선택

for k in range(3):
    # 첫 번째 집의 색이 i 일경우가 최소 값이라가 가정한 뒤, 나머지는 최대값을 지정
    for i in range(3):
        if k == i:
            dp[1][i] = arr[1][i]
        else:
            dp[1][i] = 1000 * N

    # N번 집의 색이 N-1가 달라야한다는 규칙
    # i - 1, i + 1번 집의 색이 다른 조건을 해당 규칙에 적용
    for i in range(2, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

    
    # N의 집이 1번 집의 색이 다를 경우, 최소값을 저장한다.
    for i in range(3):
        if i == k:
            continue
        answer = min(answer, dp[N][i])

print(answer)

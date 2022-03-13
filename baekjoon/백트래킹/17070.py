from sys import stdin

def check(x, y, idx):
    for direct in directions[idx]:
        dx, dy = pos[direct]
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and not arr[nx][ny]:
            if direct != 2: # 대각선이 아닐 경우
                dp[nx][ny][direct] += dp[x][y][idx]
            else: # 대각선일 경우 이동 좌표의 왼쪽과 위쪽이 비어있어야 함
                if not (arr[nx-1][ny] or arr[nx][ny-1]):
                    dp[nx][ny][direct] += dp[x][y][idx]


input = stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 3차원 내 1차원 배열은 0: 가로,1 : 세로, 2: 대각선 
# 3가지 놓인 방향에 따른 경우의 수 저장
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

# 처음 파이프는 (1,1), (1,2)를 차지하므로 2차원 행렬에서 (0, 1)의 자리에 가로방향인 0번 인덱스에 저장한다.
dp[0][1][0] = 1

# 방향별로 이동할 수 있는 방향 0: 가로,1 : 세로, 2: 대각선
# 기본 방향이 가로일 경우(0) 가로(0) 또는 대각선(2)으로만 이동 가능
directions = {0: [0, 2], 1: [1, 2], 2: [0, 1, 2]}
# 이동할 수 있는 방향에 따른 이동 좌표
pos = {0: [0, 1], 1: [1, 0], 2: [1, 1]}

for x in range(N):
    for y in range(N):
        for idx in range(3):
            if dp[x][y][idx] and not arr[x][y]:
                check(x, y, idx)

print(sum(dp[N-1][N-1]))

'''
3
0 0 0
0 0 0
0 0 0
'''

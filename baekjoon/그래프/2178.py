import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def bfs(i, j):
    global answer
    q = deque([[i, j, 1]])
    vst[i][j] = 1
    while q:
        x, y, cnt = q.popleft()
        if x == N-1 and y == M - 1:
            answer.append(cnt)
        for dx, dy in ([0, 1], [1, 0], [0, -1], [-1, 0]):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] and not vst[nx][ny]:
                    vst[nx][ny] = 1
                    q.append([nx, ny, cnt + 1])

# dfs는 시간초과 나내유

def dfs(x, y, cnt):
    global min_v
    vst[x][y] = 1
    if x == N-1 and y == M-1:
        if min_v > cnt:
            min_v = cnt
        return
    for dx, dy in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] and not vst[nx][ny] and cnt < min_v:
                vst[nx][ny] = 1
                dfs(nx, ny, cnt + 1)
                vst[nx][ny] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
vst = [[0] * M for _ in range(N)]
answer = []
min_v = 1e9
dfs(0, 0, 1)

print(min_v)

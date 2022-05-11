import sys
sys.setrecursionlimit(10**9)
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    q = deque([[i, j]])
    vst[i][j] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in ([0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] and not vst[nx][ny]:
                vst[nx][ny] = 1
                q.append([nx, ny])


def dfs(x, y):
    vst[x][y] = 1
    for dx, dy in ([0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] and not vst[nx][ny]:
            vst[nx][ny] = 1
            dfs(nx, ny)

while True:
    a = list(map(int, input().split()))
    if not a[0]:
        break
    W, H = a
    arr = [list(map(int, input().split())) for _ in range(H)]
    vst = [[0] * W for _ in range(H)]
    answer = 0
    for i in range(H):
        for j in range(W):
            if not vst[i][j] and arr[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)

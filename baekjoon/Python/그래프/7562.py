import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    global min_v
    q = deque([[i, j, 0]])
    vst[i][j] = 1
    while q:
        x, y, cnt = q.popleft()
        if x == a and  y == b:
            if min_v > cnt:
                min_v = cnt
                break
        for dx, dy in ([-1, 2], [-2, 1], [-2, -1], [-1,-2], [1, -2],[2, -1], [2, 1], [1, 2]):
            nx = x + dx
            ny = y + dy
            if 0<= nx < N and 0 <= ny < N and not vst[nx][ny]:
                vst[nx][ny] = 1
                q.append([nx, ny, cnt + 1])



T = int(input())
for tc in range(T):
    N = int(input())
    i, j = map(int, input().split())
    a, b = map(int, input().split())
    vst = [[0] * N for _ in range(N)]
    min_v = 1e9
    bfs(i, j)
    print(min_v)
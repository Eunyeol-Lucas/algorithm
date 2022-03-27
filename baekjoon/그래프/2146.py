from collections import deque
from sys import stdin
input = stdin.readline


def bfs(i, j):
    global min_v
    q = deque([[i, j, 0, arr[i][j]]])
    vst[i][j] = 1
    while q:
        x,  y, cnt, island = q.popleft()
        if cnt < min_v:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and arr[nx][ny] != island and not arr[x][y] and cnt:
                    if min_v > cnt:
                        min_v = cnt
                elif 0 <= nx < N and 0 <= ny < N and not arr[nx][ny] and cnt < min_v:
                    q.append([nx, ny, cnt + 1, island])
                elif 0 <= nx < N and 0 <= ny < N and not vst[nx][ny] and arr[nx][ny] and not cnt:
                    vst[nx][ny] = 1
                    q.append([nx, ny, cnt, arr[nx][ny]])
                elif 0 <= nx < N and 0 <= ny < N and not vst[nx][ny] and arr[nx][ny] and arr[nx][ny] == island and cnt:
                    vst[nx][ny] = 1
                    q.append([nx, ny, 0, arr[nx][ny]])


def dfs(x, y):
    global idx
    if arr[x][y] == 0:
        return
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and not ch[nx][ny] and arr[nx][ny]:
            arr[nx][ny] = idx
            ch[nx][ny] = 1
            dfs(nx, ny)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ch = [[0] * N for _ in range(N)]
vst = [[0] * N for _ in range(N)]
idx = 0
start = []
for i in range(N):
    for j in range(N):
        if not ch[i][j] and arr[i][j]:
            start.append((i, j))
            idx += 1
            ch[i][j] = 1
            arr[i][j] = idx
            dfs(i, j)
min_v = 1e9
for i in start:
    bfs(i[0], i[1])
print(min_v)

'''
5
1 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 0 0 1
'''
'''
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 1 0 0 0 0 0 0 0
'''
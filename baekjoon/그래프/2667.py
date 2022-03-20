import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    q = deque([[i, j]])
    vst[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in ([0, 1], [1, 0], [0, -1], [-1, 0]):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] and not vst[nx][ny]:
                    vst[nx][ny] = 1
                    cnt += 1
                    q.append([nx, ny])
    return cnt


def dfs(x, y):
    global count
    vsted[x][y] = 1
    count += 1
    for dx, dy in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] and not vsted[nx][ny]:
                dfs(nx, ny)


N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
vst = [[0] * N for _ in range(N)]
answer = []
for i in range(N):
    for j in range(N):
        if arr[i][j] and not vst[i][j]:
            answer.append(bfs(i, j))

result = []
vsted = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] and not vsted[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)
print(result)

print(len(answer))
for i in sorted(answer):
    print(i)

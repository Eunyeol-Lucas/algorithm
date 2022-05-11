import sys
from collections import deque

input = sys.stdin.readline


def bfs(_list):
    global answer
    q = deque(_list)
    while q:
        x, y, cnt = q.popleft()
        if answer < cnt:
            answer = cnt
        for dx, dy in ([0, 1], [1, 0], [0, -1], [-1, 0]):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    q.append([nx, ny, cnt + 1])


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
vst = [[0] * M for _ in range(N)]
tomato_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato_list.append([i, j, 0])
            vst[i][j] = 1
answer = 0
bfs(tomato_list)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            exit()
print(answer)

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    global max_v
    q = deque()
    INF = int(1e9)
    vst = [[[INF]*M for _ in range(N)] for _ in range(H)]
    for i in to_list:
        vst[i[0]][i[1]][i[2]] = 0
        q.append(i)
    while q:
        x, y, z = q.popleft()
        if vst[x][y][z] is not INF and vst[x][y][z] > max_v:
            max_v = vst[x][y][z]
        for dx, dy, dz in [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and not arr[nx][ny][nz] and vst[nx][ny][nz] == INF:
                arr[nx][ny][nz] = 1
                vst[nx][ny][nz] = vst[x][y][z] + 1
                q.append((nx, ny, nz))


M, N, H = map(int, input().split())
arr = []
to_list = []
for i in range(H):
    tmp = []
    for j in range(N):
        lst = list(map(int, input().split()))
        for k in range(M):
            if lst[k] == 1:
                to_list.append([i, j, k])
        tmp.append(lst)
    arr.append(tmp)
max_v = 0
bfs()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
print(max_v)

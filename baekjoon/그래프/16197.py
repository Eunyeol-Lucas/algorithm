from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0, coins[0][0], coins[0][1], coins[1][0], coins[1][1]))
    while q:
        cnt, x1, y1, x2, y2 = q.popleft()
        if cnt >= 10:
            return -1
        for dx, dy in drs:
            nx1 = x1 + dx
            ny1 = y1 + dy
            nx2 = x2 + dx
            ny2 = y2 + dy
            if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
                if arr[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if arr[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                q.append((cnt+1, nx1, ny1, nx2, ny2))
            elif 0 <= nx1 < N and 0 <= ny1 < M or 0 <= nx2 < N and 0 <= ny2 < M:
                return cnt + 1
    return -1


N, M = map(int, input().split())
arr = []
coins = []
for i in range(N):
    tmp = list(input().strip())
    for j in range(M):
        if tmp[j] == "o":
            coins.append([i, j])
    arr.append(tmp)
drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(bfs())

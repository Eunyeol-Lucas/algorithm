from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((0, 0))
    vst = [[0] * M for _ in range(N)]
    vst[0][0] = 1
    min_v = int(1e9)
    while q:
        x, y = q.popleft()
        if arr[x][y] == 2:
            min_v = abs(N-1-x) + abs(M-1-y) + vst[x][y] - 1
        if x == N-1 and y == M - 1:
            return min(vst[x][y] - 1, min_v)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not vst[nx][ny]:
                    if arr[nx][ny] != 1:
                        vst[nx][ny] = vst[x][y] + 1
                        q.append((nx, ny))
    return min_v


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = bfs()
print('Fail' if answer > T else answer)

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((1, 0, 0))
    vst = [[[0] * M for _ in range(N)] for _ in range(2)]
    vst[1][0][0] = 1
    while q:
        flag, x, y= q.popleft()
        if x == N-1 and y == M-1:
            return vst[flag][x][y]
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not vst[flag][nx][ny]:
                if not arr[nx][ny]:
                    vst[flag][nx][ny] = vst[flag][x][y]+1
                    q.append((flag, nx, ny))
                if arr[nx][ny] and flag:
                    vst[0][nx][ny] = vst[flag][x][y] +1
                    q.append((flag-1, nx,ny))
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
answer = bfs()
print(answer)


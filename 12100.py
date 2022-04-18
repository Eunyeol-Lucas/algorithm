from collections import deque
from copy import deepcopy

from numpy import size

def move(board, d):
    vst = [[1] * N for _ in range(N)]
    if d in {0, 3}:
        s, e, v = 0, N, 1
    else:
        s, e, v = N-1, -1, -1
    for i in range(s, e,v):
        for j in range(s, e, v):
            if board[i][j] == 0:
                continue
            x,  y = i, j
            value = board[x][y]
            nx, ny= x + drs[d][0], y + drs[d][1]
            while True:
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                if board[nx][ny] == 0:
                    x, y = nx, ny
                    nx, ny = x + drs[d][0], y + drs[d][1]
                elif board[nx][ny] == value and vst[nx][ny]:
                    x, y = nx, ny
                    vst[x][y] = 0
                    break
                else:
                    break
            board[x][y] = board[x][y] + value


def bfs(board):
    global max_v
    q = deque([board])
    v = 0
    while q:
        size = len(q)
        for _ in range(size):
            board = q.popleft()
            for d in range(4):
                tmp = move(deepcopy(board), d)
                q.append(tmp)
                for i in range(N):
                    for j in range(N):
                        if tmp[i][j] > max_v:
                            max_v = tmp[i][j]
        v += 1
        if v == 5:
            break



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
max_v = 0
bfs(arr)

print(max_v)

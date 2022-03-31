from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    global answer
    q = deque()
    q.append((0, 0))
    vst = [[-1] * (M) for _ in range(N)]
    vst[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            print(vst[x][y])
            exit()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and vst[nx][ny] == -1:
                # 빈방일 경우 그냥 지나칠 수 있으므로, 직전까지 벽을 뚫은 숫자를 그대로 가져간다.
                if arr[nx][ny] == 0:
                    vst[nx][ny] = vst[x][y]
                    # 빈방으로 이동하여 목적지까지 도착하는 경우가 가장 적게 벽을 뚫은 숫자이므로,
                    # 최소값을 찾기 위해 queue의 앞으로 추가한다.
                    q.appendleft((nx, ny))
                else:
                    # 벽일 경우 뚫고 지나가야하므로 직전까지 벽을 뚫은 숫자 + 1을 추가한다.
                    vst[nx][ny] = vst[x][y] + 1
                    q.append((nx, ny))


M, N = map(int, input().split())  # 가로, 세로
arr = [list(map(int, input().strip())) for _ in range(N)]
bfs()

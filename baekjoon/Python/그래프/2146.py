from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def bfs(i, j):
    global min_v
    q = deque([[i, j, 0, arr[i][j]]])
    vst = [[0] * N for _ in range(N)]
    vst[i][j] = 1
    while q:
        x,  y, cnt, island = q.popleft()
        # 이동 경로가 최소값보다 작을 경우에만 
        if cnt < min_v:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                # 직전 좌표가 바다이고, 이동 좌표가 섬에 방문할때 떠나온 섬과 현재 섬이 다를 경우, 최소값과 값 비교
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and arr[nx][ny] != island and not arr[x][y] and cnt:
                    if min_v > cnt:
                        min_v = cnt
                # 이동 좌표가 방문한적 없는 바다이고, 최소값 보다 현재 값이 작을 경우 방문 처리 및, 현재 좌표를 q에 추가
                elif 0 <= nx < N and 0 <= ny < N and not vst[nx][ny] and not arr[nx][ny] and cnt < min_v:
                    vst[nx][ny] = 1
                    q.append([nx, ny, cnt + 1, island])
                # 이동 좌표가 방문한적 없는 섬이며, 이동 값이 0일 때 
                elif 0 <= nx < N and 0 <= ny < N and not vst[nx][ny] and arr[nx][ny] and not cnt:
                    vst[nx][ny] = 1
                    q.append([nx, ny, cnt, arr[nx][ny]])
                # 이동 좌표가 방문한적 없는 섬이며, 출발한 섬과 같은 섬이며 이동 값이 있을 경우
                elif 0 <= nx < N and 0 <= ny < N and not vst[nx][ny] and arr[nx][ny] and arr[nx][ny] == island and cnt:
                    vst[nx][ny] = 1
                    q.append([nx, ny, 0, arr[nx][ny]])

# 지도를 순회하며 섬을 구분시켜줌
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

idx = 0
# 섬들의 시작 좌표를 저장하는 배열
start = []
for i in range(N):
    for j in range(N):
        # 방문한적 없는 섬일 경우 
        if not ch[i][j] and arr[i][j]:
            # 시작 좌표를 start 배열에 추가
            start.append((i, j))
            # 섬을 구분하기 위해 섬마다 1씩 추가된 번호를 부여
            idx += 1
            # 시작점 방문 체크 후 dfs로 섬 순회
            ch[i][j] = 1
            arr[i][j] = idx
            dfs(i, j)
min_v = 1e9
# 섬마다 최단거리 경로를 구함
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

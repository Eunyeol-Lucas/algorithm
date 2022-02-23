import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())

graph = [list(input().rstrip()) for _ in range(N)]
ch = [[0] * N for _ in range(N)]
cnt1, cnt2 = 0, 0
# 상 하 좌 우
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 현재 다음 위치가 방문하지 않은 위치인 경우 DFS를 통해 탐색
def DFS(x, y):
    if ch[y][x] == 0:
        ch[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N):
                if ch[ny][nx] == 0:
                    if graph[ny][nx] == graph[y][x]:
                        DFS(nx, ny)

# 입력받은 문자 그대로 탐색
for i in range(N):
    for j in range(N):
        if ch[i][j] == 0:
            DFS(j, i)
            cnt1 += 1

# "R"과 "G"를 하나의 문자로 변경
for i in range(N):
    for j in range(N):
        if graph[i][j] == "R":
            graph[i][j] = "G"

ch = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if ch[i][j] == 0:
            DFS(j, i)
            cnt2 += 1

print(cnt1, cnt2)

'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''

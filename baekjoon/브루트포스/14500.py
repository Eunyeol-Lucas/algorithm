from sys import stdin

# dfs 함수를 통해 인접한 행렬로 이동하며 3칸을 이동하게 되는 경우의 최대 합을 구함
def dfs(x, y, L, total):
    global answer
    # 총 3번의 행렬을 이동하는 경우 최대값을 구함
    if L == 3:
        answer = max(answer, total)
        return
    for i in range(4):
        # 현재 위치에서 우 -> 하 -> 좌 -> 상 방향으로 이동
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and ch[nx][ny] == 0:
            # 한칸 이동한 경우, ㅗ ㅜ 모양으로 이동하기 위함
            if L == 1:
                ch[nx][ny] = 1
                # 현재 이동하는 방향에서 수직으로 이동하기 위함
                dfs(x, y, L + 1, total + arr[nx][ny])
            ch[nx][ny] = 1
            dfs(nx, ny, L + 1, total + arr[nx][ny])
            ch[nx][ny] = 0


input = stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
ch = [[0] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0
for i in range(N):
    for j in range(M):
        ch[i][j] = 1
        dfs(i, j, 0, arr[i][j])
        ch[i][j] = 0

print(answer)

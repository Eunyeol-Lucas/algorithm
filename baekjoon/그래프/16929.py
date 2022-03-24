import sys
input = sys.stdin.readline

# i, j 좌표에서 출발하여 중복되는 좌표 없이 순회하여 다시 i, j로 와야한다.
def dfs(x, y, idx):
    global flag
    # 순회 좌표 x, y가 i, j 이며 회전 방향이 0이 아닐때 flag를 1로 변경한뒤 return한다.
    if x == i and y == j and idx:
        flag = 1
        return
    # 뒤로 돌아가는 경우를 제외하고 직진 또는 수직으로 방향을 회전
    for k in range(4):
        # 뒤로 돌아가는 경우는 제외
        if k != (idx + 2) % 4:
            nx = x + direction[k][0]
            ny = y + direction[k][1]
            # 아직 방문하지 않은 좌표일 경우, 직전 좌표와 값이 동일할 경우 이동
            if 0 <= nx < N and 0 <= ny < M and not flag and not vst[nx][ny]:
                if arr[x][y] == arr[nx][ny]:
                    vst[nx][ny] = 1
                    dfs(nx, ny, k)


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
flag = 0
for i in range(N-1):
    for j in range(M-1):
        vst = [[0] * M for _ in range(N)]
        dfs(i, j, 0)
        if flag:
            break
    if flag:
        break
print("Yes" if flag else "No")

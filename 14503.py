from sys import stdin
input = stdin.readline


def clean(x, y, d):
    global answer
    # 청소가 가능한 방일 경우 좌표의 값을 2로 변경한 뒤, answer + 1
    if arr[x][y] == 0:
        arr[x][y] = 2
        answer += 1
    # 이동 방향을 북동남서 순으로 만들면 현재 방향 + 3을 4로 나눈 나머지가 왼쪽 방햐
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        # 왼쪽 방향이 청소하지 않은 방일 경우, dfs 실시
        if arr[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    # 4방향 모두 이동할 수 없을 경우 뒤로 이동 가능 여부 확인
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    # 뒤가 벽일경우 종료, 이동가능할 경우 다음 좌표 방향으로 이동
    if arr[nx][ny] == 1:
        return
    clean(nx, ny, d)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
clean(R, C, D)

print(answer)

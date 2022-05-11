from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    q = deque()
    q.append((i, j))
    vst = [[0] * 6 for _ in range(12)]
    vst[i][j] = 1
    pos = [(i, j)]
    result = 0
    while q:
        x, y = q.popleft()
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 12 and 0 <= ny < 6:
                if arr[nx][ny] == arr[x][y] and not vst[nx][ny]:
                    vst[nx][ny] = 1
                    pos.append((nx, ny))
                    q.append((nx, ny))
    # 연속된 문자열을 담은 배열의 길이가 4이상일 경우 해당 좌표를 .으로 변경하고 1을 반환
    if len(pos) >= 4:
        for x, y in pos:
            arr[x][y] = '.'
        result = 1
    return result

# bfs를 통해 사라진 뿌요들의 자리를 아래에서 부터 매꿔주는 함수
def fall():
    for i in range(10, -1, -1):
        for j in range(6):
            if arr[i+1][j] == '.' and arr[i][j] != '.':
                for k in range(i+1, 12):
                    if k == 11 and arr[k][j] == '.':
                        arr[k][j] = arr[i][j]
                    elif arr[k][j] != '.':
                        arr[k-1][j] = arr[i][j]
                        break
                arr[i][j] = '.'


arr = [list(input().rstrip()) for _ in range(12)]
answer = 0
while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                cnt += bfs(i, j)
    if cnt == 0:
        print(answer)
        break
    else:
        answer += 1
        fall()

from collections import deque


def bfs():
    q = deque([(1, 0)])  # 이모티콘 수, 클립보드 이모티콘 수
    vst[1][0] = 0
    while q:
        x, y = q.popleft()
        if vst[x][x] == -1: # 방문하지 않은 경우
            # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
            vst[x][x] = vst[x][y] + 1
            q.append((x, x))
        # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣음
        if x + y <= N and vst[x+y][y] == -1:
            vst[x + y][y] = vst[x][y] + 1
            q.append((x+y, y))
        # 화면에 있는 이모티콘 중 하나를 삭제
        if x - 1 >= 0 and vst[x-1][y] == -1:
            vst[x - 1][y] = vst[x][y] + 1
            q.append((x-1, y))


N = int(input())
vst = [[-1] * (N+1) for _ in range(N+1)]
bfs()

answer = -1
for i in range(N+1):
    if vst[N][i] != -1:
        if answer == -1 or answer > vst[N][i]:
            answer = vst[N][i]
print(vst)
print(answer)

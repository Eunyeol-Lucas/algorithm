from collections import deque
# solution 1
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

# print(answer)

# solution 2


def bfs(n, c): # 화면의 이모티콘 수와, 클립보드에 저장된 이모티콘의 수를 딕셔너리에 저장
    vst[(n, c)] = True 
    dist[(n, c)] = 0
    q = deque([(n, c)])

    while q:
        s, c = q.popleft()
        if s == N:
            return dist[(s, c)]
        
        for i in [(s, s), (s+c, c), (s-1, c)]: # 복사하는 경우, 클립보드에 있는 모든 이모티콘을 화면에 붙여넣는 경우, 이모티콘 중 하나를 삭제하는 경우
            if i[0] < 0: #화면의 이모티콘 수가 0 미만인 경우 continue
                continue
            if vst.get(i, False): # 방문한적 있는 경우 continue
                continue
            q.append(i) # 이모티콘 수와 클립보의 이모티콘의 수를 q에 추가
            vst[i] = True # 방문 처리
            dist[i] = dist[(s, c)] + 1 # 시간 저장


N = int(input())

vst = {} # 임티수, 클립보드 임티 수 체크
dist = {} # 시간을 저장하는 딕셔너리
print(bfs(1, 0))

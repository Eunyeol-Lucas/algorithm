from collections import deque
import sys
input = sys.stdin.readline


def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    vst = set() # 방문 확인 속도를 향상시키기 위해 set 함수 사용
    vst.add((rx, ry, bx, by)) # 첫 빨간, 파란 구슬의 위치를 방문 set에 추가
    cnt = 0 # 움직인 횟수
    while q:
        for _ in range(len(q)): 
            rx, ry, bx, by = q.popleft()
            if cnt > 10: # 움직인 횟수가 10 초과일 경우 -1 출력 return
                print(-1)
                return
            if arr[rx][ry] == 'O': # 빨간 구슬의 현재 위치가 O 일경우 움직인 횟수 출력 return
                print(cnt)
                return
            for dx, dy in d:
                nrx, nry = rx , ry # 빨간 구술 이동 위치를 위한 변수
                while True:
                    nrx += dx
                    nry += dy
                    if arr[nrx][nry] == "#": # 벽인 경우 직전 위치로 이동
                        nrx -= dx
                        nry -= dy
                        break
                    if arr[nrx][nry] == 'O': # 구멍을 만난 경우 break
                        break
                nbx, nby = bx, by # 파란 구슬 이동 위치를 위한 변수
                while True:
                    nbx += dx
                    nby += dy
                    if arr[nbx][nby] == '#': # 벽인 경우 직전 위치로 이동
                        nbx -= dx
                        nby -= dy
                        break
                    if arr[nbx][nby] == 'O': # 구멍을 만난 경우 break
                        break
                if arr[nbx][nby] == 'O': # 파란구슬은 구멍에 빠지면 안됨으로, 해당 경우 continue
                    continue
                if nrx == nbx and nry == nby: # 이동한 위치가 빨간 구슬, 파란구슬이 동일한 경우
                    if abs(nrx -rx)  + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 이동거리가 더 먼 경우 다른 구슬 뒤에 위치 시킴
                        nrx -= dx
                        nry -= dy 
                    else:
                        nbx -= dx
                        nby -= dy
                if (nrx, nry, nbx, nby) not in vst: # 해당 이동위치가 방문한적 없는 위치일 경우 q 및 vst에 추가
                    q.append((nrx, nry, nbx, nby))
                    vst.add((nrx, nry, nbx, nby))

        cnt += 1
    print(-1)

N, M =  map(int, input().split())
arr = []
flag = 0
for i in range(N):
    tmp = list(input().rstrip())
    arr.append(tmp)
    if flag != 1: # 빨간 구슬과 파란 구슬의 위치를 모두 구하지 못했을 경우
        for j in range(M):
            if tmp[j] == 'R': # 빨간 구슬 위치
                rx, ry = i, j
                flag += 0.5
            elif tmp[j] == 'B': # 파란 구슬 위치
                bx, by = i,j
                flag += 0.5
    
d = [(0,1), (1,0), (0,-1), (-1,0)]

bfs(rx, ry, bx, by)






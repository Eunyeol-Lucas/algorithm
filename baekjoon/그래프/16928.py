from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [i for i in range(101)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] = b

q = deque()
q.append(1)
vst = [-1] * 101
vst[1] = 0

while q:
    x = q.popleft()
    for i in range(1, 7): # 주사위를 굴려 나온 값은 현재 값에 더함
        nx = x + i 
        if nx > 100: # 이동하고자하는 값이 100을 초과한 경우 pass
            continue
        v = graph[nx] # 사다리 또는 뱀을 통해 이동하거나 이동하지 않는 경우
        if vst[v] == -1: # 이동하고자 하는 곳을 아직 방문하지 않았다면 방문
            q.append(v)
            vst[v] = vst[x] + 1 # 지금까지 이동 회수 + 1을 한 값을 더해준다.
            if v == 100:
                break
print(vst[100])

from collections import deque

def bfs():
    q = deque([(N, 0)])
    vst[N] = 0
    while q:
        s, t = q.popleft()
        if 0<= s-1 < MAX and vst[s-1] == -1: # 해당 좌표에서 -1로 이동하는 경우
            vst[s-1] = t +1
            q.append((s-1, t+1))
        if 0<= 2 * s < MAX and vst[2*s] == -1: # 해당 좌표에서 좌표 * 2로 이동하는 경우
            vst[2*s] = t
            q.append((2*s, t))
        if 0<= s + 1 < MAX and vst[s+1] == -1: # 해당 좌표에서 +1로 이동하는 경우
            vst[s+1] = t + 1
            q.append((s+1, t+1))
        

N, K = map(int, input().split())
MAX = 100001
vst = [-1] * MAX
bfs()
print(vst[K])


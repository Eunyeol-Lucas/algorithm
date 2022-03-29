from collections import deque

def bfs(i):
    q = deque([[i, 0, [i]]])
    vst[i] = 1
    while q:
        x, cnt, tmp = q.popleft()
        if x == K:
            return tmp
        for j in [2*x, x+1, x-1]:
            if 0 <= j < 100001 and not vst[j]:
                q.append([j, cnt + 1, tmp + [j]])
                vst[j] = 1
    
vst = [0] * 100002
N, K = map(int, input().split()) # 수빈, 동생
print(bfs(N))
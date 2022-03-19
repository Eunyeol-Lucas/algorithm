import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline


def bfs(L):
    q = deque([L])
    vst[L] = 1

    while q:
        d = q.popleft()
        for j in graph[d]:
            if not vst[j]:
                vst[j] = 1
                q.append(j)

def dfs(L):
    vsted[L] = 1
    for i in graph[L]:
        if not vsted[i]:
            vsted[i] = 1
            dfs(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vst = [0] * (N+1)
answer = 0
for i in range(1, N+1):
    if not vst[i]:
        bfs(i)
        answer += 1

count = 0
vsted = [0] * (N+1)

for i in range(1, N+1):
    if not vsted[i]:
        dfs(i)
        count += 1

print(answer)
print(count)

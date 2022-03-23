import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(x, cnt): # 순환을 확인하는 함수
    global idx
    if x == idx and cnt >= 2:
        isCycle[idx] = 1
        return
    vst[x] = 1
    for j in graph[x]:
        if not vst[j]:
            dfs(j, cnt + 1)
        elif j == idx and cnt >= 2:
            dfs(j, cnt)


def bfs(): # 순환이 아닐 경우 가장 가까운 거리를 계산하는 함수
    q = deque()
    for i in range(1, N+1):
        if isCycle[i]:
            q.append(i)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not dis[i]:
                dis[i] = dis[x] + 1
                q.append(i)


N = int(input())
graph = [[] for _ in range(N+1)]
isCycle = [0] * (N+1)
dis = [0] * (N+1)
for i in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for idx in range(1, N+1):
    vst = [0] * (N+1)
    dfs(idx, 0)
bfs()
print(*dis[1:])

'''
6
1 2
2 3
3 4
3 5
4 6
5 6
'''
'''
5
1 2
2 3
2 4
3 5
4 5
'''

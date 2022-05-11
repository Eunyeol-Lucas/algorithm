# solution 1

import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(x, cnt):
    global idx, flag
    if x == idx and cnt >= 2:
        isCycle[idx] = 1
        flag = 1
        return
    vst[x] = 1
    for j in graph[x]:
        if not vst[j] and not flag:
            dfs(j, cnt + 1)
        elif j == idx and cnt >= 2 and not flag:
            dfs(j, cnt)


def bfs():
    q = deque()
    for i in range(1, N+1):
        if isCycle[i]:
            q.append(i)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not dis[i] and not isCycle[i]:
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
    flag = 0
    dfs(idx, 0)
bfs()
print(*dis[1:])


# solution2

import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(start, order):
    global circle
    if circle != []:
        return
    for i in graph[start]:
        if visited_dfs[i] == 0:

            visited_dfs[i] = visited_dfs[start] + 1
            dfs(i, order+[i])
            visited_dfs[i] = 0

        elif visited_dfs[start] - visited_dfs[i] != 1:
            circle = order[order.index(i):]
            return


def bfs():
    q = deque()
    for i in circle:
        q.append(i)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not dis[i] and i not in circle:
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

visited_dfs = [0] * (N+1)
circle = []
visited_dfs[1] = 1
dfs(1, [1])

bfs()
print(*dis[1:])

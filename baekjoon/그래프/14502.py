import sys
import copy
from collections import deque
input = sys.stdin.readline


def bfs():
    global answer
    tmp_graph = copy.deepcopy(graph)
    deq = deque()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                deq.append([i, j])

    while deq:
        s1, s2 = deq.popleft()

        for i in range(4):
            n1 = s1 + dx[i]
            n2 = s2 + dy[i]

            if 0 <= n1 < N and 0 <= n2 < M:
                if tmp_graph[n1][n2] == 0:
                    tmp_graph[n1][n2] = 2
                    deq.append([n1, n2])
    
    for i in range(N):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)

def dfs(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(cnt + 1)
                graph[i][j] = 0


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0
dfs(0)

print(answer)

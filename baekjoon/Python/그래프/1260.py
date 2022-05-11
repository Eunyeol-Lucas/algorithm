import sys
from collections import deque
input = sys.stdin.readline


def dfs(v):
    # V의 인접 리스트로 이동하며 방문하지 않은 노드일 경우 출력
    vst[v] = 1
    print(v, end=" ")
    for i in graph[v]:
        if not vst[i]:
            dfs(i)


def bfs(v):
    q = deque([v])
    visited = [0] * (N+1)
    while q:
        d = q.popleft()
        if not visited[d]:
            print(d, end=" ")
            visited[d] = 1
            for i in graph[d]:
                q.append(i)


N, M, V = map(int, input().split())  # 정점 개수, 간선 개수, 탐색 정점 번호
graph = [[] for _ in range(N+1)]
# 입력받은 노드에 따른 인접 리스트 생성
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순으로 정렬
for key in graph:
    key.sort()

vst = [0] * (N+1)
dfs(V)
print()
bfs(V)
print()

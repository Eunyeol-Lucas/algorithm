import heapq
import sys
input = sys.stdin.readline

N, M, C = map(int, input().split())  # 도시 개, 통로 개수, 메시지를 보내고하는 도시
INF = int(1e9)
graph = [[] for _ in range(N+1)]
for i in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
dist = [INF] * (N+1)


def dij(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        if dist[now] < dis:
            continue
        for i in graph[now]:
            cost = i[1] + dis
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dij(C)
arr = [i for i in dist if 0 < i < INF]
print(len(arr), max(arr))


'''
3 2 1
1 2 4
1 3 2
'''

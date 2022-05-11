import heapq
import sys
input = sys.stdin.readline

V, M = map(int, input().split())
graph = [[] for _ in range((V+1))]
INF = int(1e10)
dist = [[INF, 0] for _ in range(V+1)]
for i in range(M):
    a, b, c, d = map(int, input().split())  # 출발, 도착, 시간, 돈까스 맛
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))


def dij(start):
    q = []
    heapq.heappush(q, (0, 0, start))
    dist[start] = [0, 0]
    while q:
        tas, dis, now = heapq.heappop(q)
        if dist[now][0] < dis:
            continue
        for i in graph[now]:
            cost = dis + i[1]
            if (cost + tas == dist[i[0]][0] - dist[i[0]][1]) or (cost - i[2] == dist[i[0]][0] - dist[i[0]][1]):
                dist[i[0]][0] = max(dist[i[0]][0], cost)
                dist[i[0]][1] = max(i[2], dist[now][1])
                heapq.heappush(q, (-dist[i[0]][1], dist[i[0]][0],  i[0]))
            if (cost + tas < dist[i[0]][0] - dist[i[0]][1]) or (cost - i[2] < dist[i[0]][0] - dist[i[0]][1]):
                dist[i[0]][0] = cost
                dist[i[0]][1] = max(i[2], dist[now][1])
                heapq.heappush(q, (-dist[i[0]][1], cost,  i[0]))


dij(1)
for i in range(2, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i][0] - dist[i][1])

'''
6 8
1 2 3 8
1 3 4 1
2 4 4 1
3 4 4 1
2 3 2 1
4 5 2 3
3 5 5 7
1 6 25 100
'''

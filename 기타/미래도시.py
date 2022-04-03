import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())


def solution1(): # 힙큐 다익스트라
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    X, K = map(int, input().split())
    INF = int(1e9)

    def dij(start):
        q = []
        dist = [INF] * (N+1)
        heapq.heappush(q, (0, start))
        dist[start] = 0
        while q:
            dis, now = heapq.heappop(q)
            if dist[now] < dis:
                continue
            for i in graph[now]:
                cost = dis + 1
                if cost < dist[i]:
                    dist[i] = cost
                    heapq.heappush(q, (cost, i))
        return dist

    arr1 = dij(1)
    arr2 = dij(K)
    if arr1[K] + arr2[X] > INF:
        print(-1)
    else:
        print(arr1[K] + arr2[X])


def solution2(): # 플로이드 워셜
    INF = int(1e9)
    graph = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                graph[i][j] = 0

    for i in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1

    X, K = map(int, input().split())
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[k][i] + graph[k][j])

    answer = graph[1][k] + graph[K][X]
    if answer > INF:
        print(-1)
    else:
        print(answer)


solution2()

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''

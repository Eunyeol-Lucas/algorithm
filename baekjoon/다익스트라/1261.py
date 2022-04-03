import heapq
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().strip()))
    graph[i] = tmp

vst = [[0] * M for _ in range(N)]
dist = [[INF] * M for _ in range(N)]


def solution1():
    def get_smallest_node():
        min_v = INF
        index = [0, 0]
        for i in range(N):
            for j in range(M):
                if dist[i][j] < min_v and not vst[i][j]:
                    min_v = dist[i][j]
                    index = [i, j]
        return index

    def dij(i, j):
        dist[i][j] = 0
        vst[i][j] = 1
        for _ in range(N):
            for _ in range(M):
                x, y = get_smallest_node()
                vst[x][y] = 1
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < M and not vst[nx][ny]:
                        cost = dist[x][y] + graph[nx][ny]
                        if cost < dist[nx][ny]:
                            dist[nx][ny] = cost

    dij(0, 0)
    print(dist[-1][-1])


def solution2():
    def dij(i, j):
        q = []
        heapq.heappush(q, (0, i, j))
        dist[i][j] = 0
        while q:
            dis, x, y = heapq.heappop(q)
            if dist[x][y] < dis:
                continue
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    cost = dis + graph[nx][ny]
                    if cost < dist[nx][ny]:
                        dist[nx][ny] = cost
                        heapq.heappush(q, (cost, nx, ny))

    dij(0, 0)
    print(dist[-1][-1])


solution2()

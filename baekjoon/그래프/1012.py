from collections import deque


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    vst = [[0] * M for _ in range(N)]

    def bfs(k, o):
        q = deque([[k, o]])
        vst[i][j] = 1
        while q:
            x, y = q.popleft()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M and not vst[nx][ny] and graph[nx][ny]:
                    vst[nx][ny] = 1
                    q.append([nx, ny])
    result = 0
    for i in range(N):
        for j in range(M):
            if not vst[i][j] and graph[i][j]:
                bfs(i, j)
                result += 1
    print(result)

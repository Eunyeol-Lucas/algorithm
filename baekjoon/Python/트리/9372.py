def prim(start):
    vst = [0] * (N+1)
    key = [INF] * (N+1)
    key[0], key[start] = 0, 0
    for _ in range(N):
        u = 0
        min_v = INF
        for i in range(N+1):
            if vst[i] == 0 and key[i] < min_v:
                u = i
                min_v = key[i]
        vst[u] = 1
        for v in range(N+1):
            if vst[v] == 0 and graph[u][v] > 0:
                key[v] = min(key[v], graph[u][v])
    return sum(key)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split()) # 국가 수, 비행기 종류
    graph = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    INF = int(1e9)
    ans = prim(1)
    
    print(ans)
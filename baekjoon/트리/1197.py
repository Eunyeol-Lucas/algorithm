# import sys를 하지 않으면 시간초과 발생 - kruskal
def solution1():
    import sys
    input = sys.stdin.readline
    
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(x, y):
        parent[find(x)] = find(y)

    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        a, b, c = map(int, input().split())
        edge.append((c, a, b))
    edge.sort()
    parent = [i for i in range(V+1)]

    cnt = 0
    total = 0
    for c, a, b in edge:
        if cnt >= V-1:
            break
        if find(a) != find(b):
            cnt += 1
            union(a, b)
            total += c
 
    print(total)

# prim 방식은 시간 초과 발생
def solution2():
    import sys
    input = sys.stdin.readline
    INF = int(1e9)

    def prim(r, V):
        MST = [0]*(V+1)
        MST[r] = 1
        s = 0
        for _ in range(V):
            u = 0
            minV = INF
            for i in range(V+1):
                if MST[i] == 1:
                    for j in range(V+1):
                        for k in arr[i]:
                            if k[0] == j:
                                if k[1] > 0 and MST[j] == 0 and minV > k[1]:
                                    u = j
                                    minV = k[1]
            if minV < INF:
                s += minV
                MST[u] = 1
        return s

    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        arr[a].append((b, c))
        arr[b].append((a, c))
    print(prim(1, V))


solution1()

'''
3 3
1 2 1
2 3 2
1 3 3
'''

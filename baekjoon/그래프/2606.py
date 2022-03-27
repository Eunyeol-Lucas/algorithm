from sys import stdin
input = stdin.readline

N = int(input())
P = int(input())
graph = [[] for _ in range(N+1)]
vst = [0] * (N+1)
for i in range(P):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
tmp = []


def dfs(x):
    for i in graph[x]:
        if not vst[i]:
            vst[i] = 1
            tmp.append(i)
            dfs(i)


vst[1] = 1
dfs(1)
print(len(tmp))

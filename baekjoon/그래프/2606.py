from sys import stdin
input = stdin.readline

N = int(input())
P = int(input())
arr = [list(map(int, input().split())) for _ in range(P)]
graph = [[0] * (N+1) for _ in range(N+1)]
vst = [[0] * N for _ in range(N)]
for i in arr:
    graph[i[0]][i[1]] = 1
    graph[i[1]][i[0]] = 1

answer = 0

def dfs(L):
    if L==P:
        pass
        return
    else:
        
        pass


dfs(0)

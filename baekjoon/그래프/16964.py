import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, t):
    global idx, flag
    idx += 1
    if len(answer) == N:
        return
    for i in graph[x]:
        if not vst[i]:
            t.append(i)
    while t and idx < N:
        for k in range(len(t)):
            if idx < N and not vst[t[k]]:
                if t[k] == order[idx]:
                    a = t.pop(k)
                    vst[a] = 1
                    answer.append(a)
                    dfs(a, [])
                    break
        else:
            exit()


N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
order = list(map(int, input().split()))
vst = [0] * (N+1)
if order[0] != 1:
    print(0)
    exit()
answer = [order[0]]
vst[1] = 1
idx = 0
flag = 0
dfs(1, [])

print(1 if answer == order else 0)

'''
7
1 3
1 5 
3 4
2 6
3 6
4 7
1 5 3 6 2 4 7
'''

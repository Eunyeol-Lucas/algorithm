import sys
from collections import deque
input = sys.stdin.readline


def bfs(L):
    global answer
    q = deque([L])
    vst[L] = 1
    while q:
        d = q.popleft()
        for i in graph[d]:
            if not vst[i]:
                vst[i] = -1 * vst[d]
                q.append(i)
            elif vst[d] == vst[i]:
                answer = 0


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    vst = [0] * (V+1)
    answer = 1

    for i in range(1, V+1):
        if not vst[i]:
            bfs(i)
            print(vst)
            if not answer:
                break

    print("YES" if answer else "NO")

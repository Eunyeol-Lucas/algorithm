import sys
from collections import deque
input = sys.stdin.readline

def dfs():
    x = stk.popleft()
    if not stk:
        print(1)
        exit()
    vst[x] = 1
    for i in range(len(graph[x])):
        if stk[0] in graph[x] and not vst[stk[0]]:
            dfs()
    return 0

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
vst = [0] * (N+1)
order = list(map(int, input().split()))

stk = deque(order)
if stk[0] != 1:
    print(0)
    exit()

if not dfs():
    print(0)



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

'''
9
1 1
1 2
1 3
1 4 
1 5
1 6
1 7
1 8
1 2 3 4 5 6 7 8 
'''



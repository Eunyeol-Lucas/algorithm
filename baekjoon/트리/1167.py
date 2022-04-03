from collections import deque
import sys
input = sys.stdin.readline

def bfs(node):
    q = deque([node])
    score = [-1] * (N+1)
    score[node] = 0
    max_v = [0, 0]
    while q:
        x = q.popleft()
        for i, j in arr[x]:
            if score[i] == -1:
                score[i] = score[x] + j
                q.append(i)
                if max_v[0] < score[i]:
                    max_v = score[i], i
    return max_v

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-2, 2):
        arr[tmp[0]].append((tmp[i], tmp[i+1]))

s, node = bfs(1) # 임의의 지점에서 가장 멀리 위치한 노드를 구한다.
s, node = bfs(node) # 해당 기준으로 가장 멀리 떨어져있는 노드와 거리를 구한다.
print(s)
'''
6
1 3 2 -1
2 4 4 -1
3 1 2 4 3 6 10 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
3 6 10 -1
'''
'''
5
1 5 1 -1
5 1 1 4 10 -1
4 3 10 5 10 -1
3 2 10 4 10 -1
2 3 10 -1
'''

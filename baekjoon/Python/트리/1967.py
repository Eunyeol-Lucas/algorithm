from collections import deque
import sys
input = sys.stdin.readline


def bfs(node):
    q = deque()
    q.append(node)
    vst = [-1] * (N+1)
    vst[node] = 0
    max_v = [0, 0] # 가장 긴 거리와 해당 노드를 저장
    while q:
        x = q.popleft()
        for i, j in graph[x]:
            if vst[i] == -1: # 방문하지 않은 노드인 경우
                vst[i] = vst[x] + j # 직전 노드까지의 거리 + 직전 노드와 현재 노드의 거리
                q.append(i)
                if max_v[0] < vst[i]: # 현재 노드까지의 길이가 이전 가장 긴 거리보다 클 경우 재할당
                    max_v = vst[i], i

    return max_v


N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, no = bfs(1) # 임의 지점에서 가장 멀리 위치한 노드 조사
s, no = bfs(no) # 가장 멀리 위치한 노드로부터 가장 먼 거리를 구한다.
print(s)

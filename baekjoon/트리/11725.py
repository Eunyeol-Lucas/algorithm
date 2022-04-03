from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([1])
    parent = [0] * (N+1) # 부모 노드를 저장할 배열
    while q:
        now = q.popleft()
        for i in arr[now]: # 현재 노드와 연결된 노드 중
            if parent[i] == 0 and i != 1: # 연결된 노드의 부모 노드가 0이고, 연결된 노드가 1이 아닌 경우 (1은 루트 노드이기 때문)
                parent[i] = now # 연결된 노드의 부모노드는 현재 노드로 지정
                q.append(i)
    for i in range(2, N+1):
        print(parent[i])


N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
bfs()


'''
7
1 6
3 5
3 6
4 1
2 4
4 7
'''

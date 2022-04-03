import sys
input = sys.stdin.readline


def inorder(node, depth):  # 너비를 구하기 위해 중위순회를 실시
    global index
    if arr[node][0] != -1:  # 해당 노드의 왼쪽 자식 노드가 -1이 아닐 경우 다음 중위 순회 실시
        inorder(arr[node][0], depth + 1)
    graph[depth].append(index)  # 해당 노드가 위치한 index를 graph에 depth를 인덱스로 하여 추가
    index += 1
    if arr[node][1] != -1:  # 해당 노드의 오른쪽 자식 노드가 -1이 아닐 경우 다음 중위 순회 실시
        inorder(arr[node][1], depth + 1)


N = int(input().strip())
arr = [[] for _ in range(N+1)]
root = [0] * (N+1) # root 노드를 찾기위한 배열 
for i in range(N):
    a, b, c = map(int, input().split())
    for i in (a, b, c):
        if i != -1:
            root[i] += 1

    arr[a].append(b)
    arr[a].append(c)

for i in range(1, N+1):
    if root[i] == 1:
        root = i
        break

graph = [[] for _ in range(N+1)]
index = 1
inorder(root, 1)

min_depth = int(1e9)
max_v = 0
for i in range(N+1):
    if graph[i]:
        s = graph[i][0]
        l = graph[i][-1]
        if max_v < l - s + 1:
            max_v = l-s + 1
            min_depth = i
print(min_depth, max_v)

'''
6
1 2 3
2 5 4
3 -1 6
4 -1 -1
5 -1 -1
6 -1 -1
'''

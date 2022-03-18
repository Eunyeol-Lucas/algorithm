import sys
input = sys.stdin.readline

def dfs(x, L):
    global flag
    # x 인덱스 방문
    vst[x] = 1
    # 깊이가 5일 경우 flag를 1로 변경한 뒤, stop
    if L == 5:
        flag = 1
        return
    # x 인덱스를 순회하며 연결된 노드로 이동
    for i in arr[x]:
        if not vst[i]:
            dfs(i, L+1)

    vst[x] = 0


N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
vst = [0] * N
flag = 0

for i in range(N):
    dfs(i, 1)
    if flag:
        break
print(flag)

'''
6 6
0 1
1 2
2 0
3 4
4 5
5 3
'''



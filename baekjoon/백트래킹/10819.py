# dfs를 통해 가능한 조합을 모두 순회하며 계산
def dfs(L):
    global max_sum
    if L == N:
        total = 0
        for i in range(N-1):
            total += abs(tmp[i] - tmp[i+1])
        if total > max_sum:
            max_sum = total
    else:
        for i in range(0, N):
            if visited[i] == 0:
                visited[i] = 1
                tmp[L] = arr[i]
                dfs(L+1)
                visited[i] = 0


N = int(input())
arr = list(map(int, input().split()))
visited = [0] * N
tmp = [0] * N
max_sum = 0
dfs(0)

print(max_sum)

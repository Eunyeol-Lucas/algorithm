N, M = map(int, input().split())
visited = [False] * N
out = []

def backtracking(depth, N, M):
    if depth == M:
        print(" ".join(map(str, out)))
        return 
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            visited[i] = False
            backtracking(depth +1, N, M)
            out.pop()

backtracking(0, N, M)
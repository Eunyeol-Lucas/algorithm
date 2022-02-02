N, M = map(int, input().split())
visited = [False] * N
out = []

def backtracking(depth,idx, N, M):
    if depth == M:
        print(" ".join(map(str, out)))
        return 
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            backtracking(depth +1, i+1, N, M)
            visited[i] = False
            out.pop()

backtracking(0, 0, N, M)
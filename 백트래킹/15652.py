N, M = map(int, input().split())
visited = [False] * N
out = []

def backtracking(depth,idx, N, M):
    if depth == M:
        # print(depth,idx, N, M)
        print(" ".join(map(str, out)))
        return 
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            visited[i] = False
            backtracking(depth +1, i, N, M)
            
            out.pop()

backtracking(0, 0, N, M)
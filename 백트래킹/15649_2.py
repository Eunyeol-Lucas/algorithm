N, M = map(int, input().split())
visited = [False] * (N+1)
out = []

def solution(N, M):
    if len(out) == M:
        print(" ".join(map(str, out)))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            out.append(i)
            solution(N, M)
            visited[i] = False
            out.pop()

solution(N, M)
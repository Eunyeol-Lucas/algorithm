N, M = map(int, input().split())
_list = sorted(list(map(int, input().split())))
visited = [False] * N
out = []

def solution(N, M):
    if len(out) == M:
        print(" ".join(map(str, out)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            out.append(_list[i])
            solution(N, M)
            visited[i] = False
            out.pop()

solution(N, M)
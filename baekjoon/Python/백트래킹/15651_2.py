N, M = map(int, input().split())
visited = [False] * N
out = []

def solution(N, M):
    if len(out) == M:
        print(" ".join(map(str, out)))
        return
    for i in range(N):
        out.append(i+1)
        solution(N, M)
        out.pop()

solution(N, M)
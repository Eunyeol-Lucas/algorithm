N, M = map(int, input().split())
visited = [False] * N
out = []

def solution(idx, N, M):
    if len(out) == M:
        print(" ".join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(i+1)
        
        solution(i, N, M)
        out.pop()
    

solution(0, N, M)
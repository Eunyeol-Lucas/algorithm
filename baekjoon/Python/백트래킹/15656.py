N, M = map(int, input().split())
_list = sorted(list(map(int, input().split())))
out = []

def solution(N, M):
    if len(out) == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(_list[i])
        solution(N, M)
        out.pop()

solution(N, M)
N, M = map(int, input().split())
_list = sorted(list(map(int, input().split())))
out = []

def solution(idx, N, M):
    if len(out) == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(_list[i])
        solution(i, N, M)
        out.pop()

solution(0, N, M)
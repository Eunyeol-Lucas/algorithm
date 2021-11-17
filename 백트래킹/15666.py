N, M = map(int, input().split())
_list = sorted(list(map(int, input().split())))
visited = [False] * N
out = []

def solution(idx, N, M):
    if len(out) == M:
        print(' '.join(map(str, out)))
        return
    num = 0
    for i in range(idx, N):
        if num != _list[i]:
            out.append(_list[i])
            solution(i, N, M)
            num = _list[i]
            out.pop()

solution(0, N, M)
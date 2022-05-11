N, M = map(int, input().split())
_list = sorted(list(map(int, input().split())))
out = []

def solution(N, M):
    if len(out) == M:
        print(' '.join(map(str, out)))
        return
    num = 0
    for i in range(N):
        if num != _list[i]:
            out.append(_list[i])
            solution(N, M)
            num = _list[i]
            out.pop()

solution(N, M)
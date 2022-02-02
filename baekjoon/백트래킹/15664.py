N, M = map(int, input().split())
_list = sorted(list(map(int, input().split())))
visited = [False] * N
out = []

def solution(idx, N ,M):
    if len(out) == M:
        print(' '.join(map(str, out)))
        return
    num = 0
    for i in range(idx, N):
        if not visited[i] and num != _list[i]:
            visited[i] = True
            out.append(_list[i])
            num = _list[i]
            solution(i + 1, N, M)
            visited[i] = False
            out.pop()

solution(0, N, M)
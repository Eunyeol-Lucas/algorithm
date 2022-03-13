from glob import glob
from pprint import pprint


def solution(width, height):
    answer = 0
    target = width + height + 1
    end = (width + 1) * (height + 1)
    graph = [[0] * end for _ in range(end)]
    for i in range(end-1):
        graph[i][i+1] = 1
        if i+width+1 < end:
            graph[i][i+width+1] = 1

    vst = [[0] * end for _ in range(end)]

    def dfs(L, cnt):
        global answer, end
        if L == 8:
            answer += 1
            return
        else:
            for i in range(end):
                if vst[L][i] == 0 and graph[L][i] == 1 and cnt < 4:
                    vst[L][i] = 1
                    dfs(i, cnt + 1)
                    vst[L][i] = 0

    dfs(0, 0)

    return answer


pprint(solution(2, 2))

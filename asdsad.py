from pprint import pprint


def solution(width, height):
    answer = 0
    target = width + height
    end = (width + 1) * (height + 1)
    graph = [[0] * end for _ in range(end)]

    for i in range(end-1):
        graph[i][i+1] = 1
        if i+width+1 < end:
            graph[i][i+width+1] = 1

    vst = [[0] * end for _ in range(end)]

    def dfs(L, cnt):
        nonlocal answer, end, target
        if L == (end-1):
            if cnt == target:
                answer += 1
                return
        else:
            for i in range(end):
                if vst[L][i] == 0 and graph[L][i] == 1 and cnt < target:
                    vst[L][i] = 1
                    dfs(i, cnt + 1)
                    vst[L][i] = 0

    dfs(0, 0)
    answer %= 10000019
    return answer


print(solution(51, 37))

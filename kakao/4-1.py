from turtle import st


def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]

    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))

    def find(start):
        while True:
            graph[start].sort(key=lambda x: x[1])
            for i in graph[start]:
                if not vst[i[0]]:
                    vst[i[0]] = 1
                    lala.append(i[1])
                    start = i[0]
                    print(start, summits)
                    if start in summits:
                        print(lala)
                        return
                    continue

    for i in gates:
        ans = [[] for _ in range(n+1)]
        lala = []
        vst = [0] * (n+1)
        find(i)
        print(lala)

    return answer


# n = 7
# paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [
#     2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
# gates = [3, 7]
# submits = [1, 5]

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4],
         [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
print(solution(n, paths, gates, summits))
# ans = [5, 1]

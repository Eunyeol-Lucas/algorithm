INF = int(1e9)


def solution(n, paths, gates, summits):
    answer = [int(1e9), int(1e9)]

    graph = [[] for _ in range(n+1)]

    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))

    def get_smallest_node():
        min_v = INF
        index = 0
        for i in range(1, n+1):
            if dist[i] < min_v and not vst[i]:
                min_v = dist[i]
                index = i
        return index

    def dijk(start):
        dist[start] = 0
        vst[start] = 1
        for j in graph[start]:
            dist[j[0]] = j[1]
            ans[j[0]].append(j[1])
        for i in range(n-1):
            now = get_smallest_node()
            if now not in summits:
                vst[now] = True
                for j in graph[now]:
                    cost = dist[now] + j[1]
                    if cost < dist[j[0]]:
                        dist[j[0]] = cost
                        ans[j[0]] = ans[now] + [j[1]]

    for i in gates:
        vst = [0] * (n+1)
        dist = [INF] * (n+1)
        ans = [[] for _ in range(n+1)]
        dijk(i)
        print(ans)
        for j in summits:
            if i != j:
                if ans[j]:
                    if answer[1] >= max(ans[j]):
                        answer[1] = max(ans[j])
                        answer[0] = j
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

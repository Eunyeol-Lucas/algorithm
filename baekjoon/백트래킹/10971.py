from sys import stdin

input = stdin.readline


def dfs(L, M, summ):
    global min_total
    # 모든 도시를 방문한 경우
    if visited == [1] * N:
        # 마지막 도시에서 출발 도시로 가는 비용이 0이 아닐 경우
        if arr[M][L] != 0:
            # 누적된 비용에 해당 비용을 더한 값과 최소값을 비교
            min_total = min(min_total, summ + arr[M][L])
        return
    for i in range(N):
        # 현재 도시에서 다음 도시의 바용이 0이 아니고, 방문하지 않았으며, 최소값 보가 누적값이 적을 경우
        if arr[M][i] != 0 and visited[i] == 0 and summ < min_total:
            # 다음 도시를 방문
            visited[i] = 1
            dfs(L, i, summ + arr[M][i])
            visited[i] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_total = 10000000

# for문을 돌며 출발 도시를 결정
for i in range(N):
    # 도시 방문 여부 체크리스트
    visited = [0]*N
    # 출발 도시도 방문한 것이므로 해당 체크함.
    visited[i] = 1
    # 시작도시, 다음 도시, 비용
    dfs(i, i, 0)


print(min_total)

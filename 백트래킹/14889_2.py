
from itertools import combinations

N = int(input())
_list = [i for i in range(N)]
cases = list(combinations(_list, int(N/2)))
arr = [list(map(int, input().split())) for _ in range(N)]

result = int(1e9)
for start_team in cases:
    point_1 = 0
    point_2 = 0
    for i in start_team:
        for j in start_team:
            point_1 += arr[i][j]
    link_team = [i for i in range(N) if i not in start_team]
    for i in link_team:
        for j in link_team:
            point_2 += arr[i][j]
    result = min(result, abs(point_1 - point_2))
print(result)
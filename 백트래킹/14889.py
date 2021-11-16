# 시간 초과
from itertools import combinations, permutations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
dt_list = []
index = [0] * (N // 2) + [1] * (N // 2)
answer = int(1e9)

for dt in permutations(index, N):

    start_team = []
    link_team = []
    for idx, val in enumerate(dt):
        start_team.append(idx) if val == 0 else link_team.append(idx)
            
    point_1, point_2 = 0, 0

    for i in range(len(start_team)):
        for j in range(i + 1, len(start_team)): # 자기 자신의 값을 가지지 않기 위해
            point_1 += S[start_team[i]][start_team[j]] + S[start_team[j]][start_team[i]]

    for i in range(len(link_team)):
        for j in range(i + 1, len(link_team)): # 자기 자신의 값을 가지지 않기 위해
            point_2 += S[link_team[i]][link_team[j]] + S[link_team[j]][link_team[i]]
    
    answer = min(answer, abs(point_1 - point_2))

print(answer)
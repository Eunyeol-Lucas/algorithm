from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = 1e9


def get_ability(group):
    n = len(group)
    total = 0
    for i in range(n):
        a = group[i]
        for j in range(i+1, n):
            b = group[j]
            total += arr[a][b] + arr[b][a]
    return total


def team(i, team1, last):
    global min_v
    team2 = [j for j in range(N) if j not in team1]
    a1 = get_ability(team1)
    a2 = get_ability(team2)
    tmp = abs(a1 - a2)
    if tmp < min_v:
        min_v = tmp
    if a1 > a2:
        return
    else:
        for j in range(last+1, N):
            team(i+1, team1+[j], j)


team(1, [0], 0)
print(min_v)

from sys import stdin
from itertools import combinations
input = stdin.readline


def attack(_list):  # 궁수의 공격
    # 거리가 D 이하인 적 중 가장 가깝고, 적이 여러명일 경우 아장 왼쪽의 적을 공격
    target_list = []
    cnt = 0
    for i in _list:
        pos = []
        for j in range(N):
            for k in range(M):
                if tmp[j][k] == 1:
                    distance = abs(j - N) + abs(k-i)
                    if D >= distance:
                        pos.append((distance, j, k))
        pos.sort(key=lambda x: (x[0], x[2]))
        if pos:
            target_list.append(pos[0])  # 제거 리스트

    for a in target_list:
        _, i, j = a
        if tmp[i][j] == 1:
            tmp[i][j] = 0
            cnt += 1
    return cnt


def move():
    # 행렬의 마지막 -1 행부터 한칸씩 마지막 행 방향으로 이동시킴
    # 기존의 마지막 행은 전진하기 때문에 사라져야하는 행
    for i in range(-1, -N, -1):
        tmp[i] = tmp[i-1]

    tmp[0] = [0] * M


def is_empty(): # 적이 남아있는지 확인
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 1:
                return False
    return True


N, M, D = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

archer = [i for i in range(M)]
archer_list = combinations(archer, 3)
max_v = 0
for i in archer_list:
    tmp = [_list[:] for _list in maps]
    count = 0
    while not is_empty():
        count += attack(i)
        move()
    max_v = max(max_v, count)


print(max_v)

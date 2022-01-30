import sys
input = sys.stdin.readline


def solution(x, y):
    distance = y - x
    count = 0
    move = 1
    move_plus = 0
    while move_plus < distance:
        count += 1
        move_plus += move
        if count % 2 == 0:
            move += 1
    return count


for i in range(int(input())):
    x, y = map(int, input().split())
    print(solution(x, y))

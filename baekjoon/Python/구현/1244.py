import sys

input = sys.stdin.readline

# 해당 요소를 스위치하는 함수


def change(num):
    if switch_list[num] == 0:
        switch_list[num] = 1
    else:
        switch_list[num] = 0


def solution(n, sex, num):
    # 남자 일 경우 해당 요소 + 해당 요소의 배수의 자리를 변환
    if sex == 1:
        for i in range(num, len(switch_list), num):
            change(i)
    # 여자의 경우 num이 list의 절반을 넘어 갈경우 인덱스를 초과하므로
    # 절반까지 순회
    else:
        change(num)
        for i in range(n // 2):
            # 범위를 초과할 경우 break
            if num + i > n or num - i < 1:
                break
            # 배열의 num + i, num -i 요소가 일치할 경우, 스위치 시킴
            if switch_list[num+i] == switch_list[num - i]:
                change(num + i)
                change(num - i)
            else:
                break


n = int(input())
switch_list = [0] + list(map(int, input().split()))
m = int(input())
for i in range(m):
    s, num = map(int, input().split())
    solution(n, s, num)

for i in range(1, n+1):
    print(switch_list[i], end=" ")
    if i % 20 == 0:
        print()

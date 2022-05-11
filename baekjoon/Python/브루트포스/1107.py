from sys import stdin

input = stdin.readline

N = int(input())  # 이동 채널
M = int(input())  # 고장난 개수
L = 1000001
answer = abs(100 - N)

if M: # 고장난 버튼이 있을 경우 입력을 받음
    arr = list(input().split())
else: # 고장난 버튼이 없는 경우
    arr = []

# 이동할 채널과 현재 채널이 다를 경우
if answer:
    for i in range(L):
        for j in str(i):
            if j in arr: # 현재 버튼이 고장난 버튼에 포함된 경우 break
                break
        else: # 번호를 누를 수 있는 경우
            answer = min(answer, len(str(i)) + abs(i - N))
print(answer)

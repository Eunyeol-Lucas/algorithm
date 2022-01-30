import sys
input = sys.stdin.readline


def check_vps(brackets):
    stack = []
    for i in brackets:
        # 요소가 ")" 일경우 stack 배열에서 "("를 제거
        # stack에 요소가 없을 경우 vps가 아니므로 "NO"
        if i == ")":
            if stack:
                stack.pop()
            else:
                return 'NO'
        # 요소가 ")" 일 경우 stack 에 추가
        else:
            stack.append(i)
    # stack에 요소가 존재할 경우 "NO"
    if stack:
        return "NO"
    else:
        return "YES"


t = int(input())

for _ in range(t):
    brackets = input().strip()
    print(check_vps(brackets))

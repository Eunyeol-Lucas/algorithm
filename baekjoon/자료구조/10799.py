import sys
input = sys.stdin.readline


def solution(parentheses):
    answer = 0
    stack = []
    for i in range(len(parentheses)):
        # 괄호가 "("일 경우 스택에 추가
        if parentheses[i] == "(":
            stack.append("(")
        # 괄호가 ")" 일 경우
        else:
            # 스택에 존재하는 마지막 "("를 제거
            stack.pop()
            # 이전 요소가 "(" 인 경우 레이저를 발싸하여 쇠 막대기를 자름
            # 이때 스택에 ["(","(","(" ] 가 존재한다면 3조각의 쇠 막대기를 획득
            if parentheses[i - 1] == "(":
                answer += len(stack)
            # 이전 요소가 ")" 인 경우 가장 짧은 막대의 끝이므로 한 조각 추가
            else:
                answer += 1
    return answer


parentheses = input().strip()
print(solution(parentheses))

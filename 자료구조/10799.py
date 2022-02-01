import sys
input = sys.stdin.readline


def solution(parentheses):
    answer = 0
    stack = []
    for i in range(len(parentheses)):
        if parentheses[i] == "(":
            stack.append("(")
        else:
            stack.pop()
            if parentheses[i - 1] == "(":
                answer += len(stack)
            else:
                answer += 1
    return answer


parentheses = input().strip()
print(solution(parentheses))
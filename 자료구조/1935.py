import sys
input = sys.stdin.readline


def solution(postfix_notation, numbers):
    stack = []

    for i in postfix_notation:
        if i.isalpha():
            stack.append(numbers[ord(i) - 65])
        else:
            rt = stack.pop()
            lt = stack.pop()
            if i == "+":
                stack.append(lt + rt)
            elif i == "-":
                stack.append(lt - rt)
            elif i == "*":
                stack.append(lt * rt)
            elif i == "/":
                stack.append(lt / rt)
    return f'{stack[0]:.2f}'


n = int(input())
postfix = input().strip()
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)
print(solution(postfix, numbers))

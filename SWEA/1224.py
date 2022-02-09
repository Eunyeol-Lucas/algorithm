def get_postfix_notation(infix_notation):
    # 결과 출력 변수
    answer = ""
    stack = []
    for i in infix_notation:
        # 알파벷일 경우 결과 출력 변수에 추가
        if i.isdigit():
            answer += i
        else:
            if i == "(":
                stack.append(i)
            # ) 일경우 스택의 요소가 (일 때까지 pop한 뒤 결과 변수에 저장
            elif i == ")":
                while stack and (stack[-1] != "("):
                    answer += stack.pop()
                stack.pop()
            # */ 일경우 같은 우선위의 */가 스택에 존재할 경우 결과 변수에 저장
            elif i == "*" or i == "/":
                while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    answer += stack.pop()
                stack.append(i)
            # +- 의 경우 자기보다 우선순위가 높은 연산자를 결과 변수에 저장
            elif i == "+" or i == "-":
                while stack and (stack[-1] != "("):
                    answer += stack.pop()
                stack.append(i)
    # stack에 연산자가 남아 있을 경우 pop하여 결과 변수에 저장
    while stack:
        answer += stack.pop()

    return answer


def solution(postfix_notation):
    stack = []

    for i in postfix_notation:
        if i.isdigit():
            stack.append(int(i))
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
    return stack[0]

for i in range(1, 11):
    n = int(input())
    case = list(map(str, input().rstrip()))
    temp = get_postfix_notation(case)
    print(f"#{i}", solution(temp))

import sys
sys.stdin = open("input (1).txt")
T = 10

for tc in range(1, T+1):
    N = int(input())
    origin_code = list(map(int, input().split()))
    M = int(input())
    order = list(input().split()) + ["I"]
    stack = []

    for i in range(1, len(order)):
        if order[i] == "I":
            for j in range(stack[1]):
                origin_code.insert(stack[0], stack.pop())
            stack = []
        else:
            stack.append(int(order[i]))

    print(f'#{tc}', *origin_code[:10])

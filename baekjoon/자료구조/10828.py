import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        stack.append(cmd[1])
    if cmd[0] == "pop":
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    if cmd[0] == "size":
        print(len(stack))
    if cmd[0] == "empty":
        if len(stack):
            print(0)
        else:
            print(1)
    if cmd[0] == "top":
        if (len(stack)):
            print(stack[-1])
        else:
            print(-1)

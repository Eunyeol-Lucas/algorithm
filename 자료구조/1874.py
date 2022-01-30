import sys

input = sys.stdin.readline

n = int(input())
stack = []
result = []
cnt = 0
flag = True
for _ in range(n):
    num = int(input())

    while cnt < num:
        cnt += 1
        stack.append(cnt)
        result.append("+")

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = False

if flag:
    print('\n'.join(result))
else:
    print("NO")


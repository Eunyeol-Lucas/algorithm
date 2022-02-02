import sys

input = sys.stdin.readline

# 시간 초과
'''
origin = list(input().strip())
n = int(input())
index = len(origin)
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "L":
        if index:
            index -= 1
    if cmd[0] == 'D':
        if index:
            index += 1
    if cmd[0] == 'B':
        if index:
            index -= 1
            origin.remove(index)
    if cmd[0] == "P":
        origin.insert(index, cmd[1])
        index += 1
print("".join(origin))
'''

# 스택으로 풀기
origin = list(input().strip())
stack = []
n = int(input())
index = len(origin)

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "L" and origin:
        stack.append(origin.pop())
    elif cmd[0] == 'D' and stack:
        origin.append(stack.pop())
    elif cmd[0] == 'B' and origin:
        origin.pop()
    elif cmd[0] == "P":
        origin.append(cmd[1])
print("".join(origin + stack[::-1]))

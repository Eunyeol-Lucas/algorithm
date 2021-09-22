import sys
input = sys.stdin.readline
numbers = input().strip()
number = sorted(list(map(str, numbers)), reverse=True)

print(int("".join(number)))
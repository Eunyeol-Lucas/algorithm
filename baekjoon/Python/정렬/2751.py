import sys
input = sys.stdin.readline

result = []
for i in range(int(input())):
    num = int(input())
    result.append(num)

result.sort()
for i in result:
    print(i)
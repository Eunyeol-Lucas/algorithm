import sys
input = sys.stdin.readline

_list = []
for i in range(int(input())):
    a, b = map(int, input().split())
    _list.append((a, b))

new_list = sorted(_list, key=lambda x: (x[1], x[0]))
for a, b in new_list:
    print(a, b)
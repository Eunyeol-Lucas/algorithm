import sys

input = sys.stdin.readline

K = int(input())
_list = []
for i in range(K): 
    num = int(input())
    if num == 0:
        _list.pop()
    else:
        _list.append(num)

print(sum(_list) if len(_list) else 0)
import sys
input = sys.stdin.readline

n = input()
_list = list(map(int, input().split()))
list = sorted(set(_list))
result = {list[i]: i for i in range(len(list))}
print(*[result[i] for i in _list])

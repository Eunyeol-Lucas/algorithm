import sys
n = int(sys.stdin.readline())
_list = [0] * 10001
for i in range(n):
    _list[int(sys.stdin.readline())] += 1
for i in range(10001):
    if _list[i] != 0:
        for j in range(_list[i]):
            print(i)
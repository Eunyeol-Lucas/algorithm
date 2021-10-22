import sys

input = sys.stdin.readline
N, M = map(int, input().split())
_list = list(map(int, input().split()))

start, end = 0, max(_list)

while start <= end:
    mid = (start +end) // 2
    tree = 0
    for i in _list:
        if i > mid:
            tree += i - mid
    if tree >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
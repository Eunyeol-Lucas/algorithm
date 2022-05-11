import sys
import bisect

input = sys.stdin.readline

N = int(input())
_list = list(map(int, input().split()))
_list.sort()

M = int(input())
targets = list(map(int, input().split()))

result = []

for i in targets:
    left_num = bisect.bisect_left(_list, i)
    right_num = bisect.bisect_right(_list, i)

    result.append(right_num - left_num)
print(*result)
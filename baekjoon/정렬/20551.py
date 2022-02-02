import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])


def bisect_lower(_list, target):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if _list[mid] < target:
            left = mid + 1
        elif _list[mid] > target:
            right = mid - 1
        elif _list[mid] == target:
            if right == mid:
                break
            right = mid
    if _list[mid] == target:
        return mid
    return -1


for i in range(m):
    z = int(input())
    print(bisect_lower(a, z))

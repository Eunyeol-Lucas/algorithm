N = int(input())
_list = list(map(int, input().split()))
_list.sort()


def bs(target):
    left = 0
    right = len(_list) - 1
    while left < right:
        mid = (left + right) // 2
        if _list[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return 1 if _list[left] == target else 0 

_ = int(input())
_find = list(map(int, input().split()))

for dt in _find:
    print(bs(dt))
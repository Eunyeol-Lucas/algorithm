K, N = map(int, input().split())
_list = [int(input()) for _ in range(K)]


def bs(targets):
    left, right = 1, max(targets)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        lines = 0
        for i in targets:
            lines += i // mid

        if lines >= N:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    return answer

print(bs(_list))
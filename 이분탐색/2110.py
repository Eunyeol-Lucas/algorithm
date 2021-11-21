N, C = map(int, input().split())
_list = sorted([int(input()) for _ in range(N)])

def bs(targets):
    left, right = 1, targets[-1] - targets[0]
    result = 0
    while left <= right:
        mid = (left + right) // 2
        current = targets[0]
        count = 1

        for i in range(1, N):
            if targets[i] >= current + mid:
                count += 1
                current = targets[i]

        if count >= C:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    return result


print(bs(_list))
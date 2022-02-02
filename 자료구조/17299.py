import sys
input = sys.stdin.readline


def solution(n, arr):
    answer = [-1] * n
    stack = [0]

    dict = {}
    for i in arr:
        dict.setdefault(i, 0)
        dict[i] += 1

    for i in range(1, n):
        while stack and dict[arr[stack[-1]]] < dict[arr[i]]:
            answer[stack.pop()] = arr[i]
        stack.append(i)
    return answer


n = int(input())
arr = list(map(int, input().split()))
print(*solution(n, arr))

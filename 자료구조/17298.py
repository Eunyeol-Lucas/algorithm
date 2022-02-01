import sys

input = sys.stdin.readline


def solution(n, arr):
    answer = [-1] * n
    stack = [0]
    for i in range(1, n):
        # 스택의 마지막 요소를 인덱스로하는 배열의 값이 i 인덱스의 배열 값보다 클 경우
        # 스택의 마지막 요소를 인덱스로하는 answer의 값을 배열 i 인덱스 값으로 할당
        while stack and arr[stack[-1]] < arr[i]:
            answer[stack.pop()] = arr[i]
        # 현재 i(인덱스)를 스택에 추가함
        stack.append(i)
    return answer


n = int(input())
arr = list(map(int, input().split()))
print(*solution(n, arr))

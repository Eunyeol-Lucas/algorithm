import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# n번째 집까지 최소비용으로 집을 칠하기 위해서는 n-1 번째까지 최소 금액에 n번째 집을 칠하는 비용을 더한 값중 최소 값이어야 함.

result = ""
for i in range(1, n):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])
result = min(arr[n-1][0], arr[n-1][1], arr[n-1][2])
print(result)

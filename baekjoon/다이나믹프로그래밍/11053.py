import sys

input = sys.stdin.readline
A = int(input())
arr = list(map(int, input().split()))

dp = [1] * A

# arr 이 10 20 10 30 20 50 라 가정
# arr[4]가 arr[:4]까지 순위를 구해야함.
# i = 4 까지 기준으로 j = 0, 1, 2의 값보다 클 경우 dp에 해당 인덱스에 1을 더해줌
# arr[4] > arr[0] => dp[4] = max(dp[4], dp[0] +1) => 2
# arr[4] > arr[1] => dp[4] = max(2, dp[1] +1) =>2

for i in range(A):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

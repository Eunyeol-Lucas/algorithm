import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    for j in range(i):
        # 수열에서 자신보다 앞 쪽에 위치한 값 중 자신보다 작은 값의 인덱스를 찾는다.
        if arr[i] > arr[j]:
            # 해당 인덱스의 dp갑 중 가장 큰 값과 자신의 값을 더해 dp 배열을 다시 채움
            dp[i] = max(dp[i], dp[j]+arr[i])
    # 자신보다 작은 값의 인덱스가 없을 경우, 자기 자신의 값을 입력함.
    if dp[i] == 0:
        dp[i] = arr[i]
print(max(dp))

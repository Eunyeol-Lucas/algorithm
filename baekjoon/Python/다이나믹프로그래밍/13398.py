import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

total = sum(arr)
dp = [[0] * N for _ in range(2)]
# dp[0][i] : 특정 원소를 제거하지 않은 경우
# dp[1][i] : 특정 원소를 제거한 경우
dp[0][0] = arr[0]
# 원소가 1개인 경우 arr 0번 인덱스의 값은 반드시 선택됨
answer = dp[0][0]
if N > 1:
    for i in range(1, N):
        # i번 인덱스까지 아무런 원소를 제거하지 않은 경우 아래 두 수 중 큰수를 dp에 할당
            # 이전까지의 연속합 +  i번 인덱스의 원소
            # i번째의 원소
        dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
        # i번 인덱스를 제거하는 경우
        # i번째 이전에 특정 원소를 제거한 경우
        dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])
        # 큰 값을 출력 변수에 할당
        answer = max(answer, dp[0][i], dp[1][i])
print(answer)

'''
10
10 -4 3 1 5 6 -35 12 21 -1
'''


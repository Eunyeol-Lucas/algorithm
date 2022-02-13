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
# dp에 해당 요소가 몇 번째 순위인지 저장
for i in range(A):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

# dp에서 가장 큰 값은 부분 수열의 크기이다.
order = max(dp)
print(order)

_list = []
# 부분 수열을 담기 위한 배열을 선언

# 입력받은 수열을 역으로 순회
for i in range(A-1, -1, -1):
    # 가장 높은 순위일 경우
    if dp[i] == order:
        # 해당 값을 배열에 저장
        _list.append(arr[i])
        # 그 다음 순위의 값을 구하기 위해 -1을 한 뒤, 배열을 순회
        order -= 1

# 큰 수 부터 입력받았기 때문에 출력하기 위해 값을 뒤집어줌.
_list.reverse()

print(*_list)

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# 투 포인터 전략으로 문제 해결
lt = 0
sum = 0
max_sum = -1000
for rt in range(N):
    # 요소를 순회하며 sum에 값을 누적
    sum += arr[rt]
    # sum이 최대값보다 클 경우, 최대값으로 저장
    if sum > max_sum:
        max_sum = sum
    # sum이 0보다 작을 경우, 누적된 값의 왼쪽 요소부터 차례로 제거
    # sum이 0 이상일 경우에 새로운 최대값이 나타날 수 있음
    # 왼쪽 포인터가 오른쪽 포인터보다 클 경우 while문 탈출
    while lt <= rt and sum <= 0:
        sum -= arr[lt]
        lt += 1
print(max_sum)

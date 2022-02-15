import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 투포인터를 위한 왼쪽 포인터
lt = 0
# 최초 값에 k까지 요소의 합을 구함
total = sum(arr[:K])
max_sum = total

for rt in range(K, N):
    # rt가 1씩 이동함에 따라 새로운 요소를 더하고 lt 뺌
    total += arr[rt]
    total -= arr[lt]
    # lt를 다음 위치로 옭김
    lt += 1
    # 최대값을 구함.
    if total > max_sum:
        max_sum = total

print(max_sum)

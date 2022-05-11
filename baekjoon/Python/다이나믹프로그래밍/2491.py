import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

max_cnt = 1
cnt = 1
reverse_cnt = 1

for i in range(1, N):
    # 증가하는 수열을 구함
    if arr[i-1] <= arr[i]:
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    else:
        cnt = 1
    # 감소하는 수열을 구함.
    if arr[i-1] >= arr[i]:
        reverse_cnt += 1
        if max_cnt < reverse_cnt:
            max_cnt = reverse_cnt
    else:
        reverse_cnt = 1

print(max_cnt)

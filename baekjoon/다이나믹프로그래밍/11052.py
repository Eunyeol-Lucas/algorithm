import sys
input = sys.stdin.readline
n = int(input())
# 최대 값을 저장할 DP 배열
# 1부터 계산하기 위해 전체 배열에 [0]을 삽입
dy = [0] * (n+1)
arr = [0] + list(map(int, input().split()))
# 1개의 카드를 사기 위해서는 arr[1]이 최대 값임
# dy[1] = dy[0] + arr[1]
dy[1] = arr[1]

# dy[2] = dy[0]+arr[2] or dy[1] + arr[1]
# dy[3] = dy[0] +arr[3] or dy[1] + arr[2] + dy[2] + arr[1]
# dy[4] = dy[0] + arr[4] or dy[1] + arr[3] or dy[2] +arr[2] or dy[3] + arr[1]
for i in range(2, n+1):
    for j in range(1, i+1):
        if dy[i] < dy[i-j] + arr[j]:
            dy[i] = dy[i-j] + arr[j]

print(dy[n])

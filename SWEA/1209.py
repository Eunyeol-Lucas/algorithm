import sys
sys.stdin = open("SWEA/1209_input.txt")

T = 10

for tc in range(1, T+1):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    rotated_arr = list(map(list, zip(*arr)))
    diagonal1, diagonal2 = 0,  0
    max_sum = 0
    for i in range(100):
        # 열과 행을 순차적으로 합이 최고인 값을 저장
        column_sum = sum(arr[i])
        row_sum = sum(rotated_arr[i])
        max_sum = max(max_sum, column_sum, row_sum)
        # 행렬의 대각선의 합을 구함
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][99-i]
    # 최대 값을 구함
    result = max(max_sum, diagonal1, diagonal2)

    print(f"#{tc} {result}")

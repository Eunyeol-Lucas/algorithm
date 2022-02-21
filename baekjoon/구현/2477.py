import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

# 큰 사각형과 작은 사각형을 각각 구한 후, 차를 구함
# 큰 사각형: 가장 긴 가로변과 가장 긴 세로변을 구하여 면적으록 구함
# 작은 사사각형
# 최장 가로변 양 옆에는 두 개의 세로변이 존재. 이때 두 변의 차이를 구하면 작은 사각형의 면적을 알 수 있음

max_height, height_idx = 0, 0
max_width, width_idx = 0, 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if max_width < arr[i][1]:
            max_width = arr[i][1]
            width_idx = i
    else:
        if max_height < arr[i][1]:
            max_height = arr[i][1]
            height_idx = i

min_height = abs(arr[(width_idx - 1) % 6][1] - arr[(width_idx + 1) % 6][1])
min_width = abs(arr[(height_idx - 1) % 6][1] - arr[(height_idx + 1) % 6][1])
total = (max_height * max_width) - (min_height * min_width)
print(total * N)

'''
7
4 50
2 160
3 30
1 60
3 20
1 100
'''

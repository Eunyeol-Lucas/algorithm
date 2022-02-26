import sys
sys.stdin = open("SWEA/1208_input.txt")

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    while N:
        # 가장 높은 위치를 찾아서 1감소 시키고 가장 낮은 위치를 찾아서 1 감소 시킴
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
        N -= 1
    print(f'#{tc} {max(arr) - min(arr)}')

import sys
sys.stdin = open("SWEA/1206_input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    # 좌 우 2칸씩 비교하기 때문에 배열의 앞, 뒤에 [0,0] 배열을 추가해줌
    arr = [0, 0] + list(map(int, input().split())) + [0, 0]
    cnt = 0
    for i in range(2, N+2):
        # arr[i]의 view를 확인하기 위하여, arr[i] 전 후 2칸씩 건물의 높이를 하나의 배열로 만듦
        tmp = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        # tmp 배열의 최고 값을 가져와서 현재 arr[i]의 건물보다 작을 경우, 조망권이 확보가 되므로
        # 차를 구하여 조망권을 확보한 세대에 더해줌.
        max_tmp = max(tmp)
        if arr[i] > max_tmp:
            cnt += arr[i] - max_tmp

    print(f'#{tc} {cnt}')

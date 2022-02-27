import sys
sys.stdin = open("SWEA/1210_input.txt")

T = 10
for tc in range(1, T+1):
    _ = int(input())
    N = 100
    x = N - 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 도착점의 위치를 계산하여 거꾸로 출발점을 구함
    y = arr[x].index(2)

    # 행이 0이 될때 break
    while x:
        # 직진 보다 좌, 우 방향 전환이 수너임
        # 열이 0보다 클 경우, 해당 좌표의 왼쪽에 1이 있을 경우, 해당 방향으로 이동
        if y > 0:
            if arr[x][y-1] == 1:
                arr[x][y] = 0
                y -= 1
                continue
        # 열이 99보다 작을 경우, 해당 좌표의 오른쪽에 1이 있을 경우, 해당 방향으로 이동
        if y < 99:
            if arr[x][y+1] == 1:
                arr[x][y] = 0
                y += 1
                continue
        # 좌, 우에 1이 없을 경우, 앞 좌표가 1일 경우 앞으로 이동
        if arr[x-1][y] == 1:
            arr[x][y] = 0
            x -= 1

    print(f'#{tc} {y}')

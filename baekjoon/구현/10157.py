C, R = map(int, input().split())
K = int(input())

# K 가 배열안에 들어갈 숫자보다 클 경우 0을 출력
if K > C*R:
    print(0)
else:
    arr = [[0] * (C+2) for _ in range(R+2)]  # 가로 + 2, 세로 + 2
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 1, 1
    # 배열의 1,1이 오른쪽 위, 마지막 번호가 왼쪽 아래에 가도록 배열을 거울에 비춘형태로 표현
    # 번호가 배정되는 순서가 연속적으로 배열의 하 -> 우 -> 상 -> 좌 순서로 회전
    direction = 0  # 0, 1, 2, 3 (하, 우, 상, 좌)
    arr[x][y] = 1
    # 1,1 좌표에 1을 입력 이후 2부터 배열에 입력
    if K == 1:
        print(x, y)
    else:
        i = 2
        while i <= C*R:
            x += dx[direction]
            y += dy[direction]
            # 입력될 자리의 숫자가 0이며, x좌표는 1이상 C 이하이며, y 좌표가 1 이상 R 이하일 때 빈 좌석을 순서대로 채움
            if arr[y][x] == 0 and 1 <= x <= C and 1 <= y <= R:
                arr[y][x] = i
                # i가 K 일경우 좌표를 출력
                if i == K:
                    print(x, y)
                    break
                i += 1
            # if가 아닐 경우, 방향을 회전 시켜줌
            else:
                x -= dx[direction]
                y -= dy[direction]
                direction = (direction + 1) % 4

'''
1 10
1
'''

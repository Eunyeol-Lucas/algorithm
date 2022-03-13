def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    direction = 0
    vst = [[0] * n for _ in range(n)]
    origin = 1
    idx = 1

    if clockwise == True:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, 0
    else:
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        x, y = 0, n-1

    while True:
        answer[x][y] = idx

        vst[x][y] = 1
        idx += 1
        x += dx[direction]
        y += dy[direction]
        if x < 0 or x >= n or y < 0 or y >= n or vst[x][y] != 0:
            x -= dx[direction]
            y -= dy[direction]
            if direction != 3:
                answer[x][y] = origin
                idx = origin + 1

            else:
                origin = idx
                idx = origin

            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]
            if vst[x][y] == 1:
                break

    return answer


n = 6
print(solution(n, True))

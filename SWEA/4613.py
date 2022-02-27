T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_value = []

    # 리서아 국기 색 순서 흰 -> 파 -> 빨
    # 흰색 다음 파란색이, 파란색 다음 빨간색이 오도록 배치해야함.
    not_white = 0
    
    for i in range(0, N-2):
        # white가 아닌 경우 not_white 변수 1 증가
        for j in range(M):
            if arr[i][j] != "W":
                not_white += 1
        # 현재까지 흰색으로 칠한 면적 다음 파란색을 칠하는 경우
        not_blue = 0
        for j in range(i+1, N-1):
            for k in range(M):
                if arr[j][k] != "B":
                    not_blue += 1
            not_red = 0
            # 현재까지 파란색으로 칠한 면적 다음 빨간색을 칠하는 경우
            for k in range(j+1, N):
                for o in range(M):
                    if arr[k][o] != "R":
                        not_red += 1
            # white와 blue에 따라 red의 면적이 결정되므로, 이때까지 칠한 값을 tmp 변수에 합산
            tmp = not_white + not_blue + not_red
            min_value.append(tmp)
            # 그 중 최소값을 찾음.

    print(f'#{tc} {min(min_value)}')

'''
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
'''
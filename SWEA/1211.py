import sys
sys.stdin = open("SWEA/1211_input.txt")
T = 10
for tc in range(1, T+1):
    _ = input()
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    x = N - 1
    y = x

    min_cnt = 1000
    min_y = 0
    for i in range(100):
        cnt = 0
        nx, ny = 0, i
        # 왔던길을 돌아가지 않도록 방문 여부를 확인
        visited = [[0] * 100 for _ in range(100)]
        
        if arr[0][i] == 1:
            while nx < 99:
                # 1행 이후부터 좌 우측으로 방향 이동이 가능
                if nx > 0:
                    if ny > 0:
                        if arr[nx][ny-1] == 1 and visited[nx][ny-1] == 0:
                            visited[nx][ny-1] = 1
                            ny -= 1
                            cnt += 1
                            continue
                    if ny < 99:
                        if arr[nx][ny+1] == 1 and visited[nx][ny+1] == 0:
                            visited[nx][ny+1] = 1
                            ny += 1
                            cnt += 1
                            continue
                # 좌 우측으로 이동할 수 있는 경우가 아니라면 직진
                if arr[nx+1][ny] == 1 and visited[nx+1][ny] == 0:
                    visited[nx+1][ny] = 1
                    cnt += 1
                    nx += 1
            if min_cnt > cnt:
                min_cnt = cnt
                min_y = i

    print(f'#{tc} {min_y}')

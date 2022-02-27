import sys
sys.stdin = open("SWEA/11315_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    answer = 'NO'
    result = False
    # →, ↘, ↓, ↙ 순으로 순회하며 5개 연속 "o" 인경우 출력
    dx = [0, 1, 1, 1]
    dy = [1, 1, 0, -1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o":
                x, y = i, j
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                        cnt = 2
                        for _ in range(1, 4):
                            nx += dx[d]
                            ny += dy[d]
                            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                                cnt += 1
                        if cnt == 5:
                            answer = "YES"
                            break

    print(f'#{tc} {answer}')

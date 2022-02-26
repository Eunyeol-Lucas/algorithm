import sys
sys.stdin = open("SWEA/1258_input.txt")

T = int(input())

# 0이 아닌 연속된 열의 길이를 구하는 함수
def columns(i, j):
    cnt = 1
    dy = j
    while True:
        dy += 1
        if dy >= N:
            break
        if arr[i][dy]:
            cnt += 1
        else:
            break
    return cnt

# 0이 아닌 연속된 행의 길이를 구하는 함수
def rows(i, j):
    cnt = 1
    dx = i
    while True:
        dx += 1
        if dx >= N:
            break
        if arr[dx][j]:
            cnt += 1
        else:
            break
    return cnt

# 검사한 자리를 0으로 만드는 함수
def make_zero(i, j, r, c):
    for k in range(i, r):
        for o in range(j, c):
            arr[k][o] = 0


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = []

    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                c = columns(i, j)
                r = rows(i, j)
                make_zero(i, j, i+r, j+c)
                # 크기 순으로 정렬하기 위해 각 행과 열의 길이를 곱한 값을 answer 배열에 저장
                answer.append([r, c, c*r])

    # 크기 순으로 정렬하며, 크키가 같은 경우 행의 길이 순으로 정렬
    answer.sort(key=lambda x: (x[2], x[0]))

    print(f'#{tc} {len(answer)}', end=" ")
    for i, j, _ in answer:
        print(f'{i} {j}', end=" ")
    print()

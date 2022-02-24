n = int(input())

answer = 0
row = [0] * n
# 퀸을 놓지 못하는 경우
    # 같은 열에 다른 퀸이 있는 경우
    # 왼쪽 대각선, 오른쪽 대각선에 다른 퀸이 있는 경우 False를 반환
def is_possible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True


def n_queens(x):
    global answer
    # x가 최종 깊이인 n이 되면 모든 퀸을 놓았았다는 것이 되므로 1을 추가
    if x == n:
        answer += 1

    else:
        for i in range(n):
            row[x] = i
            # 퀸을 높지 못하는 경우가 아니라면 그 다음 열을 비교한다.
            if is_possible(x):
                n_queens(x+1)

n_queens(0)
print(answer)


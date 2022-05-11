from sys import stdin

input = stdin.readline

my_bingo = [list(map(int, input().split())) for _ in range(5)]
dict = {}
for i in range(5):
    for j in range(5):
        dict[my_bingo[i][j]] = [i, j]

mc_bingo = []
for _ in range(5):
    mc_bingo += list(map(int, input().split()))

bingo = 0
check_row, check_column, check_diagonal = [False] * 5, [False] * 5, [False] * 2

def check_zero_sum(arr):
    global bingo

    ZERO = [0, 0, 0, 0, 0]
    tmp_right, tmp_left = 0, 0

    for i in range(5):
        if not check_row[i] and arr[i] == ZERO:
            bingo += 1
            check_row[i] = True

        tmp_column = list(map(lambda x: x[i], arr))
        if not check_column[i] and tmp_column == ZERO:
            bingo += 1
            check_column[i] = True

        tmp_right += arr[i][i]
        tmp_left += arr[i][5-i-1]

    if not check_diagonal[0] and not tmp_right:
        check_diagonal[0] = True
        bingo += 1

    if not check_diagonal[1] and not tmp_left:
        check_diagonal[1] = True
        bingo += 1

for k in range(25):
    i, j = dict[mc_bingo[k]]
    my_bingo[i][j] = 0
    check_zero_sum(my_bingo)
    if bingo >= 3:
        print(k+1)
        exit()

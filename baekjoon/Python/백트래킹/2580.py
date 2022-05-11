# 스도쿠에 입력할 수 있는 가능한 숫자 리스트 선별 함수
def able_list(n, m):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        # 행
        if arr[n][i] in num_list:
            num_list.remove(arr[n][i])
        # 열
        if arr[i][m] in num_list:
            num_list.remove(arr[i][m])

    N = n // 3
    M = m // 3
    # 3*3 기준
    for i in range(N * 3, N * 3 + 3):
        for j in range(M * 3, M * 3 + 3):
            if arr[i][j] in num_list:
                num_list.remove(arr[i][j])
    return num_list


def dfs(L):
    if L == 81:
        return True

    for i in range(L, 81):
        N = i // 9
        M = i % 9

        if arr[N][M] != 0:
            if i == 80:
                return True
            continue

        lst = able_list(N, M)
        for j in lst:
            arr[N][M] = j
            if dfs(i+1):
                return True
            arr[N][M] = 0
        # 해당 칸에 들어갈 숫자가 없을 경우 False를 반환하고 다음 숫자를 넣음.
        return False


arr = [list(map(int, input().split())) for _ in range(9)]
dfs(0)
for i in arr:
    print(*i)

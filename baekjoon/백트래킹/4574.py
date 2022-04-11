import sys
input = sys.stdin.readline


def check(x, y, tmp):
    for i in range(9):
        if arr[x][i] == tmp:
            return False
    for i in range(9):
        if arr[i][y] == tmp:
            return False
    nx, ny = x//3 * 3, y//3 * 3
    for i in [nx, nx+1, nx+2]:
        for j in [ny, ny+1, ny+2]:
            if arr[i][j] == tmp:
                return False
    return True


def go(sudomino):
    global flag
    if len(sudomino) == 0:
        flag = 1
        print('Puzzle', idx)
        for i in arr:
            print(i)
        return
    if flag == 1:
        return
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                x, y = i, j
                for n, m in sudomino:
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 9 and 0 <= ny < 9 and arr[nx][ny]:
                            tmp = sudomino[:]
                            re_arr = (n, m)
                            tmp.remove(re_arr)

                            if check(x, y, n) and check(nx, ny, m):
                                arr[x][y], arr[nx][ny] = n, m
                                if flag == 1:
                                    return
                                go(tmp)
                                arr[x][y], arr[nx][ny] = 0, 0
                            if check(x, y, m) and check(x, y, n):
                                arr[x][y], arr[nx][ny] = m, n
                                if flag == 1:
                                    return
                                go(tmp)
                                arr[x][y], arr[nx][ny] = 0, 0


idx = 1
while True:
    N = int(input())
    print(N)
    if N == 0:
        break
    arr = [[0] * 9 for _ in range(9)]

    domino = []
    for i in range(1, 10):
        for j in range(i+1, 10):
            domino.append((i, j))

    for _ in range(N):
        U, LU, V, LV = input().split()
        U = int(U)
        V = int(V)
        x1, y1 = ord(LU[0]) - ord('A'), int(LU[1]) - 1
        x2, y2 = ord(LV[0]) - ord('A'), int(LV[1]) - 1
        arr[x1][y1], arr[x2][y2] = U, V
        if V < U:
            V, U = U, V
        domino.remove((U, V))

    for i, v in enumerate(input().split()):
        x, y = ord(v[0]) - ord('A'), int(v[1]) - 1
        arr[x][y] = i + 1

    flag = 0
    go(domino)
    idx += 1

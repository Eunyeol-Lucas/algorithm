import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input()) for _ in range(N)]

max_cnt = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(L):
    global max_cnt
    if L == 1:
        for i in range(N):
            row_cnt, column_cnt = 1, 1
            for j in range(N-1):
                if arr[i][j] == arr[i][j+1]:
                    row_cnt += 1
                    if row_cnt > max_cnt:
                        max_cnt = row_cnt
                else:
                    row_cnt = 1
                if arr[j][i] == arr[j+1][i]:
                    column_cnt += 1
                    if column_cnt > max_cnt:
                        max_cnt = column_cnt
                else:
                    column_cnt = 1
                if max_cnt == N:
                    print(max_cnt)
                    exit()
    else:
        for i in range(N):
            for j in range(N):
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[i][j] != arr[nx][ny]:
                            arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]
                            DFS(L+1)
                            arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]


DFS(0)
print(max_cnt)

'''
5
YCPZY
CYZZP
CCZPP
YCYZC
CPPZZ
'''

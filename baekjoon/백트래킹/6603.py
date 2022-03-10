from sys import stdin

input = stdin.readline


def dfs(L, s):
    # 로또 6개를 모두 고른 경우 출력
    if L == 6:
        print(*tmp)
        return
    # 중복을 없애기 위해 직전에 방문한 배열의 index 이후 배열을 순회
    for i in range(s, N):
        if visited[i] == 0:
            visited[i] = 1
            tmp[L] = arr[i]
            dfs(L+1, i)
            visited[i] = 0


while True:
    arr = list(map(int, input().split()))
    # 입력받은 값이 0일 경우 while 문을 탈출
    N = arr.pop(0)
    if N == 0:
        break
    # 조합 케이스를 담을 리스트
    tmp = [0] * 6
    # arr의 요소 체크 리스트
    visited = [0] * N

    dfs(0, 0)
    print()

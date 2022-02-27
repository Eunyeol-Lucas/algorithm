T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    answer = 0
    for i in range(N):
        mid = N//2
        # 행 열의 중앙을 기점으로 늘어나므로, 경우를 두가지로 나눔
        # 열이 mid에 가까워 질 수록 수확 범위가 늘어나므로 범위를 아래와 같이 표시
        if i <= mid:
            for j in range(mid - i, mid+1+i):
                answer += int(arr[i][j])
        # 열이 mid에서 멀어질 수록 수확 범위가 줄어드므로 범위를 아래와 같이 표시
        else:
            for j in range(i-mid, N-(i-mid)):
                answer += int(arr[i][j])

    print(f'#{tc} {answer}')

'''
1
5
14054
44250
02032
51204
52212
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    visited = [[0] * 10 for _ in range(10)]

    for i in arr:
        x, y, p, q, c = i
        for j in range(y, q+1):
            for k in range(x, p + 1):
                if visited[j][k] and c != visited[j][k]:
                    # 빨간색과 파란색이 겹친 자리를 3으로 표현 -> 보라색일 경우 cnt 1 증가
                    visited[j][k] = 3
                    answer += 1
                else:
                    visited[j][k] = c

    print(f'#{tc} {answer}')

'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''

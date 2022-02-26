T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = []
    for i in range(1, N+1):
        if not i in arr:
            answer.append(i)

    print(f'#{tc}', *answer)


'''
2
5 3
2 5 3
7 2
4 6	
    '''
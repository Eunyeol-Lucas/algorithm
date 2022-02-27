T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0
    # 성적이 가장 높은 K개의 과목 점수를 합치므로 배열에서 가장 높은 점수를 answer에 더해주고, 해당 값을 배열에서 제거
    for i in range(K):
        M = max(arr)
        answer += M
        arr.pop(arr.index(M))

    
    print(f'#{tc} {answer}')

'''
2
3 1
100 90 80
3 2
100 90 80
'''
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 0번 인덱스에서 M개의 정수를 합친 첫 배열을 생성
    tmp = sum(arr[:M])
    # 최대값과 최소값에 첫 구간을 할당
    min_sum = sum(arr[:M])
    max_sum = sum(arr[:M])

    for i in range(1, N - M+1):
        # 첫 배열의 합에서 첫 번째 값을 빼고 그 다음 값을 더해주어 그 다음 구간합을 구해줌
        tmp = tmp - arr[i-1] + arr[i+M-1]
        if max_sum < tmp:
            max_sum = tmp
        elif min_sum > tmp:
            min_sum = tmp
    print(f'#{tc} {max_sum - min_sum}')

'''
2
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
'''

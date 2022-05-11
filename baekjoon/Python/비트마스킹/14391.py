def bit_mask():
    global max_v
    # N*M 행렬로 만들 수 있는 전체 경우의수
    for i in range(1 << N * M):
        total = 0
        # 가로 합
        for r in range(N):
            # 행 내 가로의 합
            row_sum = 0
            for c in range(M):
                # 이차원 배열을 일렬로 늘렸을 때 인덱스의 위치
                idx = r * M + c  # (r행 c열)
                if i & (1 << idx):  # 비트 연산이 1일 경우 행 내 가로의 합에 추가
                    row_sum = row_sum * 10 + arr[r][c]
                else:
                    # 0일 경우, 세로의 합을 계산하므로 지금까지 나온 [행 내 가로의 합]을 total에 추가
                    # row_sum 초기화
                    total += row_sum
                    row_sum = 0
            total += row_sum

        # 세로 합 (가로합과 동일)
        for c in range(M):
            col_sum = 0
            for r in range(N):
                idx = r * M + c
                if not (i & (1 << idx)):
                    col_sum = col_sum * 10 + arr[r][c]
                else:
                    total += col_sum
                    col_sum = 0
            total += col_sum

        max_v = max(max_v, total)


N, M = map(int, input().split())  # 종이조각의 세로, 가로
arr = [list(map(int, input())) for _ in range(N)]


max_v = 0
bit_mask()
print(max_v)

'''
4 4
9090
1910
0880
3131
'''
'''
4 4 
1009
0000
1002
2401
'''
'''
4 4 
1089
0000
1002
2401
'''
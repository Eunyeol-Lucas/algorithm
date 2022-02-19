import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    if N == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        # 입력받은 2*n 2차원 배열에서 0번 인덱스까지 최대 점수는 자기 자신이다 dp[0][0] dp[1][0]
        # 1번 인덱스 까지 최대 점수는 대각선끼 값을 더한 경우이다.
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        # 2번 이상인 i번 인덱스 부터는 대각선에 위치한 i-1번 인덱스까지의 합 또는 i-2번 인덱스 까지의 합 중 최대값을 선택하여 더해줌.
        for i in range(2, N):
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])

        print(max(dp[0][N-1], dp[1][N-1]))


'''
1
2
30 50
40 10 
'''

'''
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 1260
00 20 40
20 40 30 50 60 20 80
'''
'''
1
1
1 
0 
'''

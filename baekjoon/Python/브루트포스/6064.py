from sys import stdin
input = stdin.readline

N = int(input())

for i in range(N):
    M, N, x, y = map(int, input().split())
    while x <= M*N:
        if (x - y) % N == 0:
            break
        x += M
    else:
        x = -1
    print(x)


'''
3
10 12 3 9
10 12 7 2
13 11 5 6
'''
'''
1
13 11 5 6
'''
'''
1
40000 39999 39999 39998
'''

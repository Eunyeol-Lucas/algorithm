import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * 1001 for _ in range(1001)]

for i in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for ny in range(y, y + h):
        graph[ny][x:x+w] = [i] * w

for i in range(1, n+1):
    cnt = 0
    for j in range(1001):
        cnt += graph[j].count(i)
    print(cnt)


'''
2
0 0 10 10
2 2 6 6
'''
'''
3
0 2 10 10
7 9 8 4
8 4 10 6
'''
'''
1
0 2 10 10
'''

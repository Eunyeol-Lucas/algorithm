import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr1 = sorted(arr, key=lambda x: x[0], reverse=True)
arr2 = sorted(arr, key=lambda x: x[1])
area = 0
maxH = arr2[0][1]
maxL = arr1[N-1][0] - arr1[0][0]

area = maxH * 2 + maxL
print(area)

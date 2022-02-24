import math
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

a = [0] * 7
b = [0] * 7

for i in range(N):
    s, g = map(int, input().split())
    if s == 0:
        a[g] += 1
    else:
        b[g] += 1

cnt = 0
for i in a:
    cnt += math.ceil(i/K)

for i in b:
    cnt += math.ceil(i/K)

print(cnt)

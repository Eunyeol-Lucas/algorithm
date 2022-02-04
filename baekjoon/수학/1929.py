import sys

a, b = map(int, sys.stdin.readline().split())

for i in range(a, b+1):
    idx = 0
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            idx = 1
            break
    if idx == 0:
        print(i)

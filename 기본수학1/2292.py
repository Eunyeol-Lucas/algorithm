N = int(input())
hexa = 1
cnt = 1
while N > hexa:
    hexa += 6 * cnt
    cnt += 1
print(cnt)
    
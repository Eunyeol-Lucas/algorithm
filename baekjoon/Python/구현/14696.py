import sys
input = sys.stdin.readline

# 별 > 동그라미 > 네모 > 세모 (4,3,2,1)
N = int(input())


def cal(arr):
    sum = 0
    for i in arr:
        if i == 4:
            sum += 1000000000
        elif i == 3:
            sum += 1000000
        elif i == 2:
            sum += 1000
        elif i == 1:
            sum += 1
    return sum

for i in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    
    _a = cal(a[1:])
    _b = cal(b[1:])
    if _a > _b:
        answer = "A"
    elif _a < _b:
        answer = "B"
    else:
        answer = "D"
    print(answer)
    
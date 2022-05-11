def check(L):
    total = 0
    for i in range(L, -1, -1):
        total += answer[i]
        if total == 0 and vst[i][L] != 0:
            return False
        elif total < 0 and vst[i][L] >= 0:
            return False
        elif total > 0 and vst[i][L] <= 0:
            return False
    return True


def solution(L):
    if L == N:
        return True
    if vst[L][L] == 0:
        answer[L] = 0
        return solution(L+1)
    for i in range(1, 11):
        answer[L] = vst[L][L] * i
        if check(L) and solution(L+1):
            return True
    return False


N = int(input())
arr = list(input())

vst = [[0] * N for _ in range(N)]
answer = [0] * N

for i in range(N):
    for j in range(i, N):
        tmp = arr.pop(0)
        if tmp == '+':
            vst[i][j] = 1
        elif tmp == "-":
            vst[i][j] = -1
solution(0)
print(*answer)

'''
4
-+0++++--+
'''

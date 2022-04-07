import sys
input = sys.stdin.readline

op = {
    0: lambda a, b: a + b,
    1: lambda a, b: a - b,
    2: lambda a, b: a*b,
    3: lambda a, b: a // b,
}


def dfs(L, total):
    global min_v, max_v
    if L > N:
        return
    if L == N:
        # 최소값 보다 작을 경우 갱신
        if min_v > total:
            min_v = total
        # 최대값 보다 작을 경우 갱신
        if max_v < total:
            max_v = total
        return
    for i in range(4):
        # 해당 연산자가 나눗셈이고, 현재 음수일 경우 C++14 연산으로 변경
        if i == 3 and operater[i] and total < 0:
            new = -op[i](-total, num_list[L])
            operater[i] -= 1
            dfs(L+1, new)
            operater[i] += 1
        elif operater[i]:
            new = op[i](total, num_list[L])
            operater[i] -= 1
            dfs(L+1, new)
            operater[i] += 1


N = int(input())
num_list = list(map(int, input().split()))
operater = list(map(int, input().split()))
min_v = int(1e9)
max_v = -int(1e9)
dfs(1, num_list[0])
print(max_v)
print(min_v)

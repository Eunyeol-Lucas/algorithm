N, M = map(int, input().split())
_list = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = _list[i] + _list[j] + _list[k]
            if sum > M:
                continue
            else:
                result =  max(result, sum)

print(result)

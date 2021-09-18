N = int(input())
result = []
for _ in range(N):
    x, y = map(int, input().split())
    result.append((x, y))


for i in range(N):
    rank = 1
    for j in range(N):
        if (result[i][0]!= result[j][0]) & (result[i][1] != result[j][1]):
            if (result[i][0] < result[j][0]) & (result[i][1] < result[j][1]):
                rank += 1

    print(rank)


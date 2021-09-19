N, M = map(int, input().split())
input_list = []
count = []

for _ in range(N):
    input_list.append(input())

for i in range(N-7):
    for j in range(M-7):
        not_white=0
        not_black=0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if input_list[a][b] != 'W':
                        not_white += 1
                    if input_list[a][b] != 'B':
                        not_black += 1
                else:
                    if input_list[a][b] != 'B':
                        not_white += 1
                    if input_list[a][b] != 'W':
                        not_black += 1
        count.append(min(not_white, not_black))
print(min(count))
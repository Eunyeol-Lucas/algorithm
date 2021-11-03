import sys
input = sys.stdin.readline


N, M = map(int, input().split())
data = [input() for _ in range(N)]
count = []

for i in range(N-7):
    for j in range(M-7):
        n_white = 0
        n_black = 0 
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a+b) % 2 == 0:
                    if data[a][b] != 'W':
                        n_white += 1
                    else:
                        n_black += 1
                else:
                    if data[a][b] != 'B':
                        n_white += 1
                    else:
                        n_black += 1
        count.append(min(n_white, n_black))
print(min(count))
import math

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)


N = int(input())

rep = [i for i in range(N+1)]
stars = []
edges = []

for _ in range(N):
    x, y = map(float, input().split())
    stars.append([x, y])

for i in range(N-1):
    for j in range(i+1, N):
        edges.append(
            (math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1]) ** 2), i, j))

edges.sort()

total = 0
for edge in edges:
    cost, x,  y = edge
    
    if find_set(x) != find_set(y):
        union(x, y)
        total += cost
print(f'{total:.2f}')

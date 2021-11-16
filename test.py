from itertools import permutations


data = [0,0,0,1,1,1]

for dt in permutations(data, 6):
    print(*dt)
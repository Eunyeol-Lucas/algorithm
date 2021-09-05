A, B = map(int, input().split())
for i in range(A, B+1):
    error = 0
    for j in range(2, i):
        if i % j == 0:
            error += 1
    if error == 0:
        print(i)
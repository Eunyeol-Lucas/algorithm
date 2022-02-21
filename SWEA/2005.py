T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[""] * n for i in range(n)]

    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f"#{tc}")
    for i in arr:
        print(*i)
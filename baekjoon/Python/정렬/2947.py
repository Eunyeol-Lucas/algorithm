arr = list(map(int, input().split()))

while True:
    if arr == [1, 2, 3, 4, 5]:
        break
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
        print(*arr)
    if arr[1] > arr[2]:
        arr[1], arr[2] = arr[2], arr[1]
        print(*arr)
    if arr[2] > arr[3]:
        arr[2], arr[3] = arr[3], arr[2]
        print(*arr)
    if arr[3] > arr[4]:
        arr[3], arr[4] = arr[4], arr[3]
        print(*arr)

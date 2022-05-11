from sys import stdin

input = stdin.readline
N = int(input())
S = 0
for i in range(N):
    arr = input().split()

    if arr[0] == "add":
        S |= (1 << int(arr[1]) )
    if arr[0] == "remove":
        S &= ~(1 << int(arr[1]))
    if arr[0] == "check":
        print(1 if S & (1 << int(arr[1])) else 0)
    if arr[0] == "toggle":
        S ^= (1 << int(arr[1]))
    if arr[0] == "all":
        S = (1 << 21) - 1
    if arr[0] == "empty":
        S = 0

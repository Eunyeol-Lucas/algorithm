n = int(input())
arr = list(map(int, input().split()))
s = [1]
for i in range(1, n):
    s.insert(arr[i], i+1)
print(*s[::-1])

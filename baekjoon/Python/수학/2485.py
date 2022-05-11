import sys
input = sys.stdin.readline

def gcd(a, b):
    if (b==0):
        return a
    else:
        return gcd(b, a%b)

N = int(input())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)

dist = []
for i in range(N-1):
    dist.append(abs(arr[i+1] - arr[i]))

tmp = dist[0]
for i in dist:
    tmp = gcd(tmp, i)

len_arr = (max(arr)-min(arr)) // tmp + 1
print(len_arr - len(arr))
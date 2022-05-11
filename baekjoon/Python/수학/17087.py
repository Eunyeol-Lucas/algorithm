import sys

input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, (x % y)
    return x


# 수빈이가 있는 위치에서 동생둘이 있는 위치 차이값들의 최대 공약수를 구함.
n, s = map(int, input().split())
positions = list(map(int, input().split()))
minus_positions = list(set([abs(positions[i]-s) for i in range(n)]))
max_distance = min(minus_positions)
for i in range(len(minus_positions)):
    max_distance = gcd(minus_positions[i], max_distance)
print(max_distance)

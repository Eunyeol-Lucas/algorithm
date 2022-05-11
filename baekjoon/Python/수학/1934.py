import sys
from math import gcd
input = sys.stdin.readline

def lcm(x, y):
    return x * y // gcd(x, y)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))

import sys
a, b = map(int, sys.stdin.readline().split())

# 유클리드 호제법
# 1에서 x와 y 중 작은 값의 범위에서 공약수를 모두 구한 다음 이 수들 중 최대값을 구하는 방법
def gcd(x, y):
    while y:
        x, y = y, (x % y)
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(a, b))
print(lcm(a, b))

import sys

input = sys.stdin.readline

MAX = 499999
is_prime = [0, 0, 1] + [1, 0] * MAX
prime_index = []
for i in range(2, 1000001):
    if is_prime[i]:
        prime_index.append(i)
        for j in range(i*2, 1000001, i):
            is_prime[j] = 0


def get_count(n):
    result = 0
    for i in prime_index:
        tmp = n - i
        if i > tmp:
            break
        else:
            if is_prime[tmp]:
                result += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    print(get_count(n))

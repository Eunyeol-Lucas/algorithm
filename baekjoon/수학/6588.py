import sys
input = sys.stdin.readline


def isPrime(num):
    idx = 0
    for j in range(2, int(num**0.5)+1):
        if num % j == 0:
            idx = 1
            break
    return idx


def getPrime(num):
    prime_list = []
    for i in range(2, num):
        if isPrime(i) == 0:
            b = num - i
            if isPrime(b) == 0:
                return f'{num} = {i} + {b}'


while True:
    even = int(input())
    if even == 0:
        break
    print(getPrime(even))

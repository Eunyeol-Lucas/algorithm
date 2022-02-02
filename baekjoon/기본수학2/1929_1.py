A, B = map(int, input().split())

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

for i in range(A, B+1):
    if isPrime(i):
        print(i)
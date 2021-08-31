num = int(input())
numbers = map(int, input().split())
prime = 0
for number in numbers:
    no_prime = 0
    if number > 1:
        for i in range(2, number):
            if number%i == 0:
                no_prime += 1
        if no_prime == 0:
            prime += 1
print(prime)
import random


def make_random(a, b):
    print(a, b)
    for i in range(b):
        print(random.randrange(10**a, 10**(a+1)))


make_random(4, 4)

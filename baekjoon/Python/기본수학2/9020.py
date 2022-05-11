def prime():
    prime_list = [False]*2 + [True]*9999
    for i in range(2, 101):
        if prime_list[i] == True:
            for j in range(2*i, 10001, i):
                prime_list[j] = False

    num = int(input())
    for _ in range(num):
        prime_num = int(input())

        A = prime_num // 2
        B = A
        for _ in range(10000):
            if prime_list[A] and prime_list[B]:
                print(A, B)
                break
            A -=1
            B += 1
    
prime()
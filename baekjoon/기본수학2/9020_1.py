num_list = [1]*10001
num_list


def prime_plus(n):
    num_list = prime_list(n)
    idx = len(num_list)
    for i in range(idx, -1, -1):
        for j in range(i, idx):
            if num_list[i]+num_list[j] == n:
                return [num_list[i], num_list[j]]
            else:
                continue

for i in range(int(input())):
    num = int(input())
    prime = prime_plus(num)
    print(prime)
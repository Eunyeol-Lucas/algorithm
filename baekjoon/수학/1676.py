import sys

n = int(sys.stdin.readline())


def get_factorial(num):
    if num <= 1:
        return 1
    return num*get_factorial(num-1)


def get_count_zero(num):
    cnt = 0
    for i in str(get_factorial(num))[::-1]:
        if i == "0":
            cnt += 1
        else:
            break
    return cnt


print(get_count_zero(n))

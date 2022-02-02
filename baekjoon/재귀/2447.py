import sys
input = sys.stdin.readline

n = int(input())


def recursion(num):
    if num == 1:
        return ["*"]
    stars = recursion(num//3)
    star_list = []
    for s in stars:
        star_list.append(s*3)
    for s in stars:
        star_list.append(s + " "*(num//3) + s)
    for s in stars:
        star_list.append(s*3)
    return star_list


print('\n'.join(recursion(n)))

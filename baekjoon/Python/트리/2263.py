import sys
sys.setrecursionlimit(10**9)

N = int(input())
in_list = list(map(int, input().split()))
post_list = list(map(int, input().split()))
lst = [0] * (N+1)
for i in range(N):
    lst[in_list[i]] = i


def pre_order(in_l, in_r, post_l, post_r):
    if post_l <= post_r:
        parents = post_list[post_r]

        print(parents, end=" ")
        p_index = lst[parents]
        l_count = p_index-in_l
        r_count = in_r-p_index

        pre_order(in_l, in_l + l_count-1, post_l, post_l+l_count-1)
        pre_order(in_r-r_count+1, in_r, post_r - r_count, post_r-1)


pre_order(0, N-1, 0, N-1)

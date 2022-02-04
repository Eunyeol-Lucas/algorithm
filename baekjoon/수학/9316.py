import sys
from math import gcd

input = sys.stdin.readline

# 리스트 내 모든 조합으로 최대공약수를 구함
def get_sum_gcd(arr):
    total = 0
    for i in range(1, len(arr)):
        for j in range(i + 1, len(arr)):
            total += gcd(arr[i], arr[j])
    return(total)


t = int(input())
for _ in range(t):
    _list = list(map(int, input().split()))
    print(get_sum_gcd(_list))

import sys
from collections import Counter

input = sys.stdin.readline

N = input()
_set = list(map(int, input().split()))
M = input()
_list = list(map(int, input().split()))

C = Counter(_set)
print(' '.join(f'{C[num]}' if num in C else '0' for num in _list))
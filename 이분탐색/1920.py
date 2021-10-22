import sys

input = sys.stdin.readline
N = int(input())
_set = set(map(int, input().split()))
M = int(input())
_list = list(map(int, input().split()))

print(*[1 if num in _set else 0 for num in _list], sep="\n") 
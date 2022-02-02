import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

_dict = { str(i + 1): input() for i in range(N)}
_reversed = dict(map(reversed, _dict.items()))

for _ in range(M):
    K = input()
    print(_dict[K]) if K in _dict else print(_reversed[K])
import sys
input = sys.stdin.readline

result = []
for _ in range(int(input())):
    a, b = map(str, input().split())
    result.append((int(a), b))

_result = sorted(result, key = lambda x: x[0])
for a, b in _result:
    print(a, b)

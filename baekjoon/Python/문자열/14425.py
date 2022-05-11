import sys

input = sys.stdin.readline

N,M  = map(int, input().split())

_set = {input() for _ in range(N)}

answer = 0
for _ in range(M):
    if input() in  _set:
        answer += 1
    
print(answer)
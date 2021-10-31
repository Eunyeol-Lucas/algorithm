import sys
from collections import deque

input = sys.stdin.readline
deq = deque([])

for _ in range(int(input())):
    q = input().split()
    if q[0] == "push":
        deq.append(q[1])
    if q[0] == "pop":
        print(-1) if not deq else print(deq.popleft())
    if q[0] == "size":
        print(len(deq))
    if q[0] == "empty":
        print(1) if not deq else print(0)
    if q[0] == "front":
        print(-1) if not deq else print(deq[0])
    if q[0] == "back":
        print(-1) if not deq else print(deq[-1])
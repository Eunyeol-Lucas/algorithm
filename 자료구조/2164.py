from collections import deque

dq = deque(range(1, int(input()) + 1))

while len(dq) != 1:
    dq.popleft()
    dq.rotate(-1)

print(dq[0])

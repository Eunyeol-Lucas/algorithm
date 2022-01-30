import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = [str(i) for i in range(1, n+1)]
result = []
num = 0
while queue:
    num = (num + (k-1)) % len(queue)
    result.append(queue.pop(num))

print('<{}>'.format(', '.join(result)))

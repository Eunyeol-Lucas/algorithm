import sys
import heapq

input = sys.stdin.readline
N = int(input())
_list = list(map(int, input().split()))
heapq.heapify(_list)

for _ in range(N-1):
    new_list = list(map(int, input().split()))
    for i in range(N):
        heapq.heappushpop(_list, new_list[i])

print(heapq.heappop(_list))
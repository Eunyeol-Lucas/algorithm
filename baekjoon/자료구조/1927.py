import sys
import heapq

input = sys.stdin.readline

_list =[]
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        print(heapq.heappop(_list)) if len(_list) else print(0)
    else:
        heapq.heappush(_list, num)
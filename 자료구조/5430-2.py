import sys
from collections import deque

input = sys.stdin.readline

def solution():
    p = input().rstrip()
    _ = input().rstrip()
    arr = deque(input().rstrip().strip('[]').split(','))

    flag = 0
    for i in p:
        if i == "D":
            if not arr or not arr[0]:
                print('error')
                return
            if flag == 0:
                arr.popleft()
            else:
                arr.pop()
        else:
            flag = 1 - flag
    
    print('[' + ','.join(arr) + ']') if flag == 0 else print('[' + ','.join(list(arr)[::-1])+ ']')

for i in range(int(input())):
    solution()
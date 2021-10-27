from collections import deque
import sys 

input = sys.stdin.readline

def solution():
    func = input().rstrip()
    _ = input().rstrip()
    arr = deque(input().rstrip().strip('[]').split(','))

    flag = 0
    for c in func:
        if c == "D":
            if not arr or not arr[0]:
                print('error')
                return
            if flag == 0:
                arr.popleft()
            else:
                arr.pop()
        else:
            flag = 1 - flag
    if flag == 0:
        print('[' + ','.join(arr) + ']')
    else:
        print('[' + ','.join(list(arr)[::-1]) + ']')



for i in range(int(input())):
    solution()
import sys
import heapq
input = sys.stdin.readline

def solution(_list):
    left, right = [], []
    middle = _list[0]
    result = [middle]
    for idx, val in enumerate(_list[1:], 1):
        if val > middle:
            heapq.heappush(right, val)
        else:
            heapq.heappush(left, -val)
        if idx % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -middle)
                middle = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, middle)
                middle = -heapq.heappop(left)
            result.append(middle)
    print(len(result))

    for i in range(len(result)):
        if (i + 1) != 1 and (i + 1)%10 == 1:
            print()
        print(result[i], end=" ")
    


        
for _ in range(int(input())):
    count = int(input())
    _list = []

    if count % 10 == 0:
        for _ in range(count // 10):
            _list.extend(list(map(int, input().rstrip().split())))
    else:
        for _ in range(count//10 + 1):
            _list.extend(list(map(int, input().rstrip().split())))

    solution(_list)

'''
3
9
1 2 3 4 5 6 7 8 9
9
9 8 7 6 5 4 3 2 1
23
23 41 13 22 -3 24 -31 -11 -8 -7 3 5 103 211 -311 -45 -67 -73 -81 -99 -33 24 56
'''
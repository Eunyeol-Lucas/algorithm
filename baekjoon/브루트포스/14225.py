import heapq

def solution1():
    N = int(input())
    arr = list(map(int, input().split()))

    dict = {}
    for i in range(1 << N):
        tmp = 0
        for j in range(N):
            if i & (1 << j):
                tmp += arr[j]
        dict[tmp] = 1

    a = sorted(list(dict.keys()))
    k = a[0]
    ans = a[-1]+1
    for i in range(1, len(a)):
        if a[i] - k > 1:
            ans = k+1
            break
        else:
            k = a[i]
    print(ans)

def solution2():
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = 0
    flag = 1
    q = []
    heapq.heappush(q, (0, 0))
    if arr[0] > 1:
        print(1)
        exit()
    while q:
        x, cnt = heapq.heappop(q)
        if cnt == ans + 1:
            ans = cnt
        elif cnt > ans + 2:
            print(ans+1)
            flag = 0
            break
        if x < N:
            heapq.heappush(q, (x+1, cnt + arr[x]))
            heapq.heappush(q, (x+1, cnt))
    if flag:
        print(sum(arr)+1)
'''
3
5 1 2
'''

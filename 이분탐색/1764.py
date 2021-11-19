N, M = map(int, input().split())
listen_arr = sorted([input() for _ in range(N)])
see_arr = [input() for _ in range(M)]

def bs(target):    
    result = []
    for i in target:
        left = 0
        right = len(listen_arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if listen_arr[mid] > i:
                right = mid - 1
            elif listen_arr[mid] < i:
                left = mid + 1
            else:
                result.append(i)
                break  
    return sorted(result)

answer = bs(see_arr) 
print(len(answer))
for i in answer:
    print(i)
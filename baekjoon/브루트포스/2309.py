import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
answer = []
# 배열을 복사한 뒤, 배열의 앞에서부터 2개씩 제거하여 합이 100인 배열을 구함.
for i in range(9):
    for j in range(i+1, 9):
        new_arr = arr[:]
        new_arr.pop(j)
        new_arr.pop(i)
        if sum(new_arr) == 100:
            answer = new_arr
            break

# 오름차순으로 정렬
answer.sort()
for i in answer:
    print(i)


'''
20
7
23
19
10
15
25
8
13
'''

# 다음 순열 (Next Permutation)
N = int(input())
arr = list(map(int, input().split()))
swap = -1

# 입력받은 순열을 뒤에서부터 순회하며 값이 작아지는 구간이 있는 지 확인
# 값이 작아지는 구간이 있다면 해당 구간의 index를 저장해둠 (swap 변수에 할당)
# 값이 작아지는 구간이 없다면 내림차순으로 정렬된 것이므로 -1을 반환
for i in range(N-1, 0, -1):
    if arr[i-1] < arr[i]:
        swap = i - 1
        break
else:
    print(-1)
    exit()

# 순열을 입력한 배열을 역순으로 순회
# i번째가 인덱스 swap 번째 수보다 클 경우, 두 수의 위치를 바꿈
# 바꾼 위치를 기준으로 인덱스 swap 이후의 수를 오름차순으로 정렬
for i in range(N-1, 0, -1):
    if arr[swap] < arr[i]:
        arr[swap], arr[i] = arr[i], arr[swap]
        arr = arr[:swap+1] + sorted(arr[swap+1:])
        print(*arr)
        break

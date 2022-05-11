import sys

input = sys.stdin.readline

N = int(input())
# 입력 받은 배열를 x 좌표를 기준으로 정렬
arr = sorted([list(map(int, input().split())) for _ in range(N)])
# 마지막 x값과 y값은 배열의 최초 요소를 할당
last_idx, last_height = arr[0]
# 면적을 저장할 변수
area = 0
while True:
    # 최대 높이값을 가진 인덱스와 높이를 0,0으로 초기화
    max_idx, max_height = 0, 0
    # 마지막 인덱스와 높이의 요소 다음 값부터 순회하며, 현재 높이가 마지막 높이보다 클 경우 멈추고 넓이를 구해줌.
    for i in range(arr.index([last_idx, last_height])+1, N):
        cur_idx, cur_height = arr[i]
        if cur_height > last_height:
            area += (cur_idx-last_idx) * last_height
            last_idx, last_height = cur_idx, cur_height
            break
        if cur_height > max_height:
            max_idx, max_height = cur_idx, cur_height
    
    # 끝까지 순회했을 때 현재 높이값보다 큰 값이 나오지 않으면 현재 높이를 더하고, 이후 가장 큰 막대를 기준으로 나머지 넓이를 구해줌.
    else:
        area += last_height + (max_idx - last_idx - 1) * max_height
        last_idx, last_height = max_idx, max_height
        if last_idx == 0:
            break
print(area)

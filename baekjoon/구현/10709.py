H, W = map(int, input().split())

for i in range(H):
    arr = list(input())
    # 결과를 입력할 result 배열을 선언하어 기본값으로 -1을 할당
    result = [-1] * W
    check = []
    # 배열의 순서대로 최신 "c"의 인덱스를 저장
    C = 0
    for j in range(W):
        # 앞에 구름이 포함된 구 인지 확인하기 위해 check 배열에 입력
        check.append(arr[j])
        # check 배열에 구름이 있고, 현재 값이 구름이 아니라면 현재 위치의 서쪽에 구름이 위치
        # 해당 구름이 몇분뒤에 도착하는지는 'c'인덱스와 자신의 구역의 인덱스의 차
        if "c" in check and arr[j] != "c":
            result[j] = j - C
        # c일 경우 result 배열에 0을 삽입한 뒤, 최신 구름의 인덱스로 재할당
        if arr[j] == "c":
            result[j] = 0
            C = j

    print(*result)

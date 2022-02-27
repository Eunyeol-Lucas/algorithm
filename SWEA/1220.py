import sys
sys.stdin = open("SWEA/1220_input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        tmp = []
        for j in range(N):
            # 열단위로 나누어 요소가 1 또는 2인 경우 임시 배열에 추가
            if arr[j][i] == 1 or arr[j][i] == 2:
                tmp.append(arr[j][i])
        # 열에 극성이 한개만 존재할 경우 테이블 아래로 떨어지므로 1 초과 경우
        if len(tmp) > 1:
            for k in range(len(tmp)-1):
                # 교착상태는 N극과 S극이 맞닿을 경우 1 증가하므로 1과 2가 연속해서 배열에 위치한 경우 1증가
                if tmp[k] == 1 and tmp[k+1] == 2:
                    cnt += 1

    print(f'#{tc} {cnt}')

import sys
input = sys.stdin.readline

N = int(input())
D = int(input()) # 다솜이 득표수
arr = [int(input()) for _ in range(N-1)] # 다솜이 제외한 국회의원 후보 득표수 배열

cnt = 0
# 참가자가 다솜이 혼자가 아닌 경우
if N != 1:
    while True:
        # 다솜이가 다른 후보들보다 득표수가 많으면 break
        if D > max(arr):
            break
        else:
            # 배열에서 최다 득표수를 선택
            tmp = max(arr)
            # 최다 득표수를 1개 감소 시키고 다솜이에게 추가시킴
            tmp -= 1
            # 감소시킨 득표수를 다시 그 값에 할당
            arr[arr.index(max(arr))] = tmp
            D += 1
            cnt += 1

print(cnt)

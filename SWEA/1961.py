import sys
sys.stdin = open("SWEA/1961_input.txt")

T = int(input())

# 90도씩 회전한 행렬을 만드는 함수
def rotate(arr):
    rotate_arr = []
    for i in range(N):
        tmp = []
        for j in range(N-1, -1, -1):
            tmp.append(arr[j][i])
        rotate_arr.append(tmp)
    return rotate_arr


for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    r_arr = rotate(arr)
    rr_arr = rotate(r_arr)
    rrr_arr = rotate(rr_arr)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(r_arr[i]), ''.join(rr_arr[i]), ''.join(rrr_arr[i]))

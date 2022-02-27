import sys
sys.stdin = open("SWEA/1215_input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    C = 8
    arr = [list(input()) for _ in range(C)]
    reverse_arr = list(map(list, zip(*arr)))
    cnt = 0

    for i in range(C):
        for j in range(C-N+1):
            # 문자열을 뒤집은 문자열과 일치할 경우 cnt + 1
            tmp = arr[i][j:j+N]
            if tmp == tmp[::-1]:
                cnt += 1
            reverse_tmp = reverse_arr[i][j:j+N]
            if reverse_tmp == reverse_tmp[::-1]:
                cnt += 1

    print(f"#{tc} {cnt}")

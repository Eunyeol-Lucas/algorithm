import sys
sys.stdin = open("SWEA/1959_input.txt")

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # A와 B의 배열 길이의 차 + 1만큼 곱하기의 합을 구해야함
    N = abs(a-b) + 1
    value_list = [0] * N

    for i in range(N):
        # a가 b보다 클 경우
        if a > b:
            for j in range(b):
                value_list[i] += A[i+j] * B[j]
        # b가 a보다 크거나 같을 경우
        else:
            for j in range(a):
                value_list[i] += B[i+j] * A[j]

    print(f"#{tc} {max(value_list)}")

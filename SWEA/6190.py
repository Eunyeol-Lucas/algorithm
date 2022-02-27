T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = -1
    for i in range(N-1):
        for j in range(i+1, N):
            M = arr[i] * arr[j]
            if answer < M:
                str1 = str(M)
                # 연속된 숫자가 단조 숫자가 아닐 경우 break
                for k in range(len(str1)-1):
                    if str1[k] > str1[k+1]:
                        break
                # 단조 숫자가 최대값일 경우 최대값에 할당
                else:
                    if answer < M:
                        answer = M

    print(f'#{tc} {answer}')


'''
1
4
1245 6834 1127 10
'''
'''
1
3
1 1 1
'''

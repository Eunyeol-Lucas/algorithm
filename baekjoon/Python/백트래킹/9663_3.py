def dfs(y):
    global cnt
    if y == N:
        cnt += 1
        return 1

    for x in range(N):
        # 좌표기준 위아래, 대각선 방향으로 퀸이 없는 경우
        if vst[x] == vst2[y+x] == vst3[x-y] == 0:
            # 방문체크
            vst[x] = vst2[y+x] = vst3[x-y] = 1
            # cnt 1을 더한경우 다시 0으로 돌린뒤 break
            if dfs(y+1):
                vst[x] = vst2[y+x] = vst3[x-y] = 0
                break
            vst[x] = vst2[y+x] = vst3[x-y] = 0
    return 0


N = int(input())
cnt = 0
vst = [0] * N
vst2 = [0] * (N * 2 - 1)
vst3 = [0] * (N * 2 - 1)

for j in range(N // 2): # 체스의 대칭성을 이용하여 절반의 이동 횟수를 구한 후 *2를 해줌
    vst[j] = vst2[j] = vst3[j] = 1
    dfs(1)
    vst[j] = vst2[j] = vst3[j] = 0
cnt *= 2
if N % 2: # 크기가 홀수일 경우 중간을 기준으로 DFS를 통해 길이를 구해줌
    j = N // 2
    vst[j] = vst2[j] = vst3[j] = 1
    dfs(1)
print(cnt)

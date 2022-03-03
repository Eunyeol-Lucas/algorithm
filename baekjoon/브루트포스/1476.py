E, S, M = map(int, input().split())

# 모두 같은 시간이 프르므로, 세 수가 같은 값을 가질 때까지 각 행성별 최대 범위의 값을 더해준다.
while True:
    if E == S and S == M:
        break
    if E < S or E < M:
        E += 15
        continue
    if S < E or S < M:
        S += 28
        continue
    if M < E or M < S:
        M += 19
        continue

print(E)

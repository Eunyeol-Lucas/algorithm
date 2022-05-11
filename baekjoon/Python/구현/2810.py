N = int(input())
str = list(input())

# 좌석 끝에는 컵홀더가 있으므로 cnt에 2를 할당하여 선언
cnt = 2

# 오른쪽 끝은 S또는 L 상관없이 우측에 컵홀더가 있으므로 제외하고 계산
for i in range(N-1):
    # S 좌석의 경우 우측에 컵홀더가 있다고 가정하여 cnt 1 증가
    if str[i] == "S":
        cnt += 1
    # LL의 경우에만 우측에 한개의 컵홀더가 존재하므로 cnt 1증가
    elif str[i] == "L" and str[i-1] == "L":
        str[i] = "S"
        cnt += 1

if cnt > N:
    print(N)
else: print(cnt)

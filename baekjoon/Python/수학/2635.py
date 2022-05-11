import sys

result = 0
arr = []
n = int(sys.stdin.readline())
# 입력 받은 n의 절반 이하의 수는 for문을 돌면 바로 종결되기 때문에 절반 이상의 수부터 for문 순회
for i in range(n//2, n+1):
    # 두 번째 정수
    second_num = i
    # 입력받은 n과 두 번째 정수를 무조건 포함하기 때문에 임시 count를 2 할당
    cnt = 2
    first_num = n
    tmp_arr = [first_num, second_num]

    while True:
        first_num, second_num = second_num, first_num - second_num
        # 두 수의 차가 0 미만일 경우 while문을 종료
        if second_num < 0:
            break
        tmp_arr.append(second_num)
        cnt += 1
    # 누적된 count가 result보다 클 경우 result에 cnt를, arr에 임시 배열을 할당
    if cnt > result:
        result = cnt
        arr = tmp_arr

print(result)
print(*arr)

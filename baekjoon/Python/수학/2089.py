# 10진수를 -2진수로 변환하는 문제
import sys

n = int(sys.stdin.readline())
# 출력될 2진수를 담는 변수
result = ""
while n:
    quotient = n // -2
    # -2진수로 나누었을 때 나머지가 0-1, 0, 1이 나오므로 -1이 나오는 경우 몫에 1을 더해줌
    # 이때 나머지가 0 또는 1로 바뀜
    if n % -2 < 0:
        quotient += 1
    # 나머지를 결과 문자열에 추가
    result += str(n - (quotient * -2))
    n = quotient

if result:
    # 역으로 뒤집어서 출력
    print(result[::-1])
else:
    print(0)

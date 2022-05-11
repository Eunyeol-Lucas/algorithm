import sys
import string
n, b = map(int, sys.stdin.readline().split())

#  0부터 Z까지 더한 문자열을 만듦
alpha = string.digits + string.ascii_uppercase
result = ""
# while문을 통해 나머지는 result에 더하고 몫을 계속해서 진수로 나눔.
while n:
    result += alpha[n % b]
    n = n // b
# 출력하기 전 문자열을 뒤집어줌
print(result[:: -1])

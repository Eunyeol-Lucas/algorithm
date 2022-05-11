"""
왜 틀린지 모르겠음.
import math
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
_list = list(map(int, input().split()))
ten_number = 0
result = []

for i in range(m):
    ten_number += int(_list[i] * math.pow(a, m - i - 1))
answer = ""
while ten_number:
    answer += str(ten_number % b)
    ten_number //= b

print(*answer[::-1])"""




import math
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
_list = list(map(int, input().split()))
ten_number = 0
result = []

for i in range(m):
    ten_number += int(_list[i] * math.pow(a, m - i - 1))

answer = ""
while ten_number:
    result.append(str(ten_number % b))
    ten_number //= b


print(*result[::-1])

'''
처음부터 최대 1억자리 까지 더해주기 때문에 당연히 시간초과
N = int(input())

answer = ""
for i in range(1, N+1):
    answer += str(i)

print(len(answer))
'''


# 자리수의 합을 계산해서 풀어야하는 문제
# 1부터 9까지 1자리의수의 합은 9
# 10부터 99까지 2자리수의 합은 90
# 100부터 999까지 3자리수의 합은 900
# 이런 규칙을 통해 주어진 숫자의 자리수보다 하나 작은 자리수까지 길이를 구한 뒤
# 입력받은 수  - (입력받수 - 이전까지 자리수의 합 + 1 )* 자리수 규칙을 통해 계싼
N = input()
length = len(N)
answer = 0

for i in range(length-1):
    answer += 9*(10**i)*(i+1)

print(answer + (int(N) - 10**(length-1) + 1) * length)

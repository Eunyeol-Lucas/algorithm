# itertools combination 조합은 시간 초과로 인해 불가
import sys
input = sys.stdin.readline

# 조합 내의 0의 개수를 구하는 문제로, 지수의 차와 팩토리얼 내 0을 만들 수 있는 2와 5를 활용
def get_count_zero(n, num):
    count = 0
    numerator = num
    while n >= numerator:
        count += (n // numerator)
        numerator *= num
    return count


m, n = map(int, input().split())
# 0의 개수: M!이 가지고 있는 2개의 개수 - N!이 가지고 있는 2의 개수 - (M-N)!이 가지고 있는 2의 개수
# M!이 가지고 있는 5의 개수 - N!이 가지고 있는 5의 개수 - (M-N)!이 가지고 있는 5개의 개수 중 작은 수
print(min(get_count_zero(m, 5) - get_count_zero(n, 5) - get_count_zero(m-n, 5),
      get_count_zero(m, 2) - get_count_zero(n, 2) - get_count_zero(m-n, 2)))

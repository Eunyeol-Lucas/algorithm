w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# p + t는 t초 동안 x축 0에서 개미가 이동한 위치를 의미 -> w로 나누면 개미가 0 - w 사이에서 몇 번 왕복했는지 도출
# q + t도 y축 0을 기준으로 총 이동한 거리

a = (p + t) // w
b = (q + t) // h

# t초 후의 개미 위치를 알기 위해선 a와 b가 홀수 인지 짝수인지 에 따라 다름.
# 0을 기준으로 이동한 거리 / w가 
    #  짝수 인 경우 왕복 후 남은 값은 0점을 기준으로 이동한 위치
    #  홀수 인 경우 왕복 후 남은 값은 h 또는 w를 기준으로 음수로 이동한 위치

if a % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w
if b % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h
print(x, y)

# 시간초과
# dx = 1
# dy = 1

# for _ in range(t):
#     p += dx
#     q += dy
#     t -= 1
#     if (p == w and q == h) or (p == 0 and q == 0):
#         dx = -1
#         dy = -1
#     elif p == w or p == 0:
#         dx *= -1
#     elif q == h or q == 0:
#         dy *= -1

# print(p, q)


'''
6 4
4 1
8
'''

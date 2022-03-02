A, B = map(int, input().split())
C = int(input())
time, min = 0, 0

# 분 B와 C의 합이 60 이상일 경우, 시 단위로 바뀌기 때문에 
# 합의 몫을 시 A에 더해주고, 24시가 넘을 경우 0으로 변경되기 때문에
# 24로 나눈 나머지를 time에 할당
time = (A + (B+C)//60) % 24
min = (B+C) % 60
print(time, min)

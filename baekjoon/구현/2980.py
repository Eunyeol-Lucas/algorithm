import sys
sys = sys.stdin.readline

N, L = map(int, input().split())

time = 0  # 누적 시간
location = 0  # 최초 위치

for _ in range(N):
    D, R, G = map(int, input().split())
    # 시간을 마지막 위치에서 현재 위치까지 이동시 걸린 시간을 기록
    time += (D - location)
    location = D
    # 현재 시간을 (빨간불+ 초록불)로 나눈 나머지가 빨간불의 시간보다 적다면 기다려야 하고
    # 기다리는 시간만큼 추가해줌
    if time % (R+G) <= R:
        time += (R - (time % (R+G)))
# L 위치까지 마지막 위치에서 이동한 시간을 더해줌
time += (L-location)
print(time)

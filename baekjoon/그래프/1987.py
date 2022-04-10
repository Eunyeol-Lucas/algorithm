import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
max_v = 1
q = set() # set을 써야만 통과가 가능하다
q.add((0, 0, arr[0][0]))
while q:
    x, y, track = q.pop()
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx = x +dx
        ny = y + dy
        # 아직 지나치지 않은 알파벳 일 경우에만 다음 칸으로 이동 가능
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] not in track:
            q.add((nx, ny, track + arr[nx][ny]))
            max_v = max(max_v, len(track)+1)

print(max_v)

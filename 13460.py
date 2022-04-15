import sys
input = sys.stdin.readline

def bfs():


N, M =  map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
vst = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
d = [(0,1), (1,0), (0,-1), (-1,0)]







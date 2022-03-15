front = rear = 0

def enq(a, b):
    global rear, Q
    rear = (rear+1) % len(Q)
    Q[rear] = (a, b)

def deq():
    global front, Q
    if isEmp():
        return 'Q is empty'
    else:
        front = (front+1) % len(Q)
        return Q[front]

def isEmp():
    global front, rear
    return front == rear

def maze():
    global la, N, M, front, rear, Q
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    while not isEmp():
        p = deq()
        I, J = p[0], p[1]
        t = la[I][J]

        for k in range(4):
            if 0 <= I+dx[k] <= M-1 and 0 <= J+dy[k] <= N-1:

                if la[I+dx[k]][J+dy[k]] == 0:
                    enq(I+dx[k], J+dy[k])
                    la[I+dx[k]][J+dy[k]] = t+1

    for i in range(M):
        for j in range(N):
            if la[i][j] == 0:
                return -1
    return t-1


N, M = map(int, input().split())
la = [list(map(int, input().split())) for _ in range(M)]
Q = [(0, 0)]*N*M

for i in range(M):
    for j in range(N):
        if la[i][j] == 1:
            enq(i, j)

print(maze())

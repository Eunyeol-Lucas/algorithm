# 1차 풀이
N = int(input())
answer = 0

def solution(data):
    global answer
    if len(data)== N:
        print(data)
        answer += 1
        return
    for i in range(1, N + 1):
        flag = True
        for j in range(len(data)):
            if data[j] == i or len(data) - j == abs(i - data[j]):
                flag = False
                break
        if flag:
            data.append(i)
            solution(data)
            data.pop()

solution([])
print(answer)        

# 2차 풀이
N = int(input())
answer = 0


def solution(data):
    global answer
    if len(data) == N:
        answer += 1
        return
    for i in range(1, N + 1):
        flag = True
        for j in range(len(data)):
            if data[j] == i or len(data) - j == abs(i - data[j]):
                flag = False
                break
        if flag:
            data.append(i)
            solution(data)
            data.pop()


for i in range(1, (N//2+1)):
    solution([i])
answer *= 2
if N % 2:
    solution([N//2+1])
print(answer)

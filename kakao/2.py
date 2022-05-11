from collections import deque

def bfs(q1, q2):
    q = deque()
    q.append((q1, q2, 0))
    opp = len(q1) + len(q2)
    min_v = int(1e9)
    while q:
        q3, q4, cnt = q.popleft()
        if q3 and q4:
            if sum(q3) == sum(q4):
                if min_v > cnt:
                    min_v = cnt
            if cnt > opp:
                break
            if cnt < min_v:
                q5 = q3[:]
                q6 = q4[:]
                q6.append(q5.pop(0))
                q.append((q5, q6, cnt + 1))
                q7 = q3[:]
                q8 = q4[:]
                q7.append(q8.pop(0))
                q.append((q7, q8, cnt + 1))
    return min_v


def solution(queue1, queue2):
    answer = -1
    result = bfs(queue1, queue2)
    if result != int(1e9):
        answer = result

    return answer

# b1 = [3, 2, 7, 2]
# b2 = [4, 6, 5, 1]
# b1 = [1, 1]
# b2 = [1, 5]
b1 = [1, 2, 1, 2]
b2 = [1, 10, 1, 2]
print(solution(b1, b2))

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(order[0])
    # 입력받은 BFS 순서가 1이 아닐 경우 0 return
    if order[0] != 1:
        return 0
    # 방문체크 리스트
    vst = [0] * (N+1)
    # 처음 입력받은 BFS 0번 인덱스 방문
    vst[order[0]] = 1
    # q에 입력되는 문자와 BFS 배열을 비교하기 위한 index
    idx = 0
    while q:
        x = q.popleft()
        # x 노드에서 이동할 수 있는 노드를 담을 임시 배열
        tmp = []
        for i in graph[x]:
            # 방문하지 않은 경우
            if not vst[i]:
                # 방문 체크 후 tmp 배열에 요소 추가
                vst[i] = 1
                tmp.append(i)
        # tmp 배열에 요소가 있을 경우
        if len(tmp):
            # 해당 요소와 위치가 동일한 입력받은 BFS 순서 배열을 가져옴
            lst = order[idx+1:idx+1+len(tmp)]
            # tmp 배열과 BFS 배열을 오름차순으로 정렬하여 일치할 경우 q에 저장
            if sorted(tmp) == sorted(lst):
                for j in lst:
                    q.append(j)
                # index를 tmp 배열 길이만큼 추가
                idx += len(tmp)
                # 임시배열을 초기화함
                tmp = []
            # 일치하지 않을 경우 해당 노드와 간선으로 BFS 순서를 만들지 못하므로 0을 반환
            else:
                return 0
    return 1


N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
order = list(map(int, input().split()))
answer = bfs()
print(answer)


'''
4
1 2
1 3
2 4
1 3 2 4
'''
'''
4
1 2
1 3
2 4
1 2 4 3
'''
'''
5
1 2
1 3
2 4
3 5
1 3 2 5 4
'''
'''
11
2 1
2 5
4 3
4 7
1 4
5 6
8 10
8 9
9 11
6 8
2 5 1 6 4 8 7 9 3 10 11
'''
'''
7
1 2
1 3
2 4
2 5
3 6
3 7
1 2 3 4 5 6 7
'''
'''
7
1 2
1 3
2 4
2 5
3 6
3 7
1 3 2 6 7 4 5
'''
'''
7
1 2
1 3
2 4
2 5
3 6
3 7
1 2 3 6 7 4 5
'''
'''
9
2 3
2 1
1 4
3 5
3 6
3 7
3 8
3 9
2 3 1 5 6 7 8 9 4
'''
'''
6
1 2
3 4
5 6
2 3
4 5
1 2 3 4 5 6
'''
'''
6
1 2
3 4
5 6
2 3
4 5
1 2 3 5 6 4
'''
'''
10
1 2
2 3
2 4
3 5
1 7
7 10
6 8
6 9
1 6
1 7 6 2 10 9 8 4 3 5
'''

from sys import stdin
input = stdin.readline

N = int(input())
arr = list(input().split())

tmp = []
vst = [0] * 10
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# 부등호 조건에 맞는 배열을 모두 담을 배열
_list = []


def dfs(L):
    # 재귀 레벨이 N+1일 경우 임시 배열을 조건 배열에 담음
    if L == (N+1):
        _list.append(tmp[:])
        return
    for i in range(10):
        # 임시 배열이 비어있을 경우
        if not tmp:
            vst[i] = 1
            tmp.append(num_list[i])
            dfs(L+1)
            vst[i] = 0
            tmp.pop()
        else:
            # 임시 배열에 값이 들어있고, 해당 인덱스를 방문하지 않은 경우
            if vst[i] == 0:
                # 부등호가 < 일 때 임시 배열의 마지막 요소가 현재 값보다 작을 때
                if arr[L-1] == "<":
                    if tmp[-1] < num_list[i]:
                        tmp.append(num_list[i])
                        vst[i] = 1
                        dfs(L+1)
                        vst[i] = 0
                        tmp.pop()
                # 부등호가 > 일 때 임시 배열의 마지막 요소가 현재 값보다 클 때
                else:
                    if tmp[-1] > num_list[i]:
                        tmp.append(num_list[i])
                        vst[i] = 1
                        dfs(L+1)
                        vst[i] = 0
                        tmp.pop()


dfs(0)
print(''.join(_list[-1]))
print(''.join(_list[0]))

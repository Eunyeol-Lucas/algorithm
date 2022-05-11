from sys import stdin
input = stdin.readline

L, C = map(int, input().split())
arr = sorted(list(input().split()))
tmp = []
# 모음만 들어있는 리스트 생성
alp = ["a", "e", "i", "o", 'u']
vst = [0] * C

# V : 재귀 레벨, W : index, a: 모음 수, b: 자음 수
def dfs(V, W, a, b):
    # 재귀레벨이 L이고, 모음이 하나 이상, 자음이 두개 이상일 경우 출력
    if V == L and a >= 1 and b >= 2:
        print("".join(tmp))
        return
    for i in range(W, C):
        # 임시 배열이 빈 배열일 경우
        if not tmp:
            # 해당 인덱스의 요소가 모음일 경우, 모음 개수 + 1, 자음일 경우 자음 개수 + 1
            if arr[i] in alp:
                a += 1
            else:
                b += 1
            tmp.append(arr[i])
            vst[i] = 1
            dfs(V+1, i, a, b)
            # 재귀가 끝난 경우 -1 해줌
            if arr[i] in alp:
                a -= 1
            else:
                b -= 1
            vst[i] = 0
            tmp.pop()
        else:
            # 아직 요소를 배열에 추가하지 않고, 임시 배열의 마지막 요소보다 현재 요소가 클 경우
            if vst[i] == 0 and tmp[-1] < arr[i]:
                if arr[i] in alp:
                    a += 1
                else:
                    b += 1
                vst[i] = 1
                tmp.append(arr[i])
                dfs(V+1, i, a, b)
                if arr[i] in alp:
                    a -= 1
                else:
                    b -= 1
                vst[i] = 0
                tmp.pop()


dfs(0, 0, 0, 0)

'''
5 6
a i e u s w
'''

from sys import stdin
input = stdin.readline

L, C = map(int, input().split())
arr = sorted(list(input().split()))
tmp = []
alp = ["a", "e", "i", "o", 'U']
vst = [0] * C


def dfs(V, W, a, b):
    if V == L and a >= 1 and b >= 2:
        print("".join(tmp))
        return
    for i in range(W, C):
        if not tmp:
            if arr[i] in alp:
                a += 1
            else:
                b += 1
            tmp.append(arr[i])
            vst[i] = 1
            dfs(V+1, i, a, b)
            if arr[i] in alp:
                a -= 1
            else:
                b -= 1
            vst[i] = 0
            tmp.pop()
        else:
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
4 6
a i e u s w
'''

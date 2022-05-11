num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def dfs(L, num):
    global flag
    if L > N:
        return
    if flag:
        if L == N:
            flag = 0
            print(num)
            return
        for i in cal:
            if not vst[i]:
                if (arr[L] == "<" and num[L] < num_list[i]) or (arr[L] == ">" and num[L] > num_list[i]):
                    vst[i] = 1
                    dfs(L+1, num+num_list[i])
                    vst[i] = 0


N = int(input())
arr = list(input().split())
vst = [0] * 10

for i in range(9, -1, -1):
    flag = 1
    vst[i] = 1
    cal = range(9, -1, -1)
    dfs(0, num_list[i])
    vst[i] = 0
    if not flag:
        break

for i in range(10):
    flag = 1
    vst[i] = 1
    cal = range(10)
    dfs(0, num_list[i])
    vst[i] = 0
    if not flag:
        break

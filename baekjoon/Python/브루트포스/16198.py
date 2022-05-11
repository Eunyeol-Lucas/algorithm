N = int(input())
arr = list(map(int, input().split()))
answer = 0
def dfs(v):
    global answer 
    # 배열의 길이가 2일 때 값이 최대값 보다 클 경우, 값을 갱신한다.
    if len(arr) == 2:
        if answer < v:
            answer = v
            return
    for i in range(1, len(arr)-1):
        # i 인덱스를 기준으로 앞 뒤의 값을 곱하고, 그 값을 v에 더한다.
        v += arr[i-1]*arr[i+1]
        # i 인덱스의 숫자를 임시로 저장해 둔뒤 제거하여 재귀를 반복한다.
        tmp = arr[i]
        del arr[i]
        dfs(v)
        # 삭제한 요소를 재귀가 끝났을 때 다시 삽입하여 원상복구하고, v에 더한 값을 다시 제거한다.
        arr.insert(i, tmp)
        v -= arr[i-1]*arr[i+1]
dfs(0)
print(answer)
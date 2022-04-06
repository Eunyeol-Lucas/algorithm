from collections import defaultdict

N = int(input())
arr = [input() for _ in range(N)]
dict = defaultdict(int)
total = 0
idx = 9
for i in range(N):
    length = len(arr[i])
    for j in range(length):
        # 10 ** (문자의 위치 - 1) 를 하여 문자열의 위치한 자리수를 계산하여 dict에 저장
        dict[arr[i][j]] += 10 ** (length-j-1)

# 내림차순으로 정렬
num_list = sorted(list(dict.values()), reverse=True)
for i in num_list:
    # 자리수 * idx를 해주어 가장 큰 수를 만들어 준다. idx는 9에서 0으로 역순으로 떨어짐.
    total += idx * i
    idx -= 1
print(total)

from itertools import combinations as cb
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# anta, tica는 반드시 들어가야하는 글자로, 해당 알파벳을 set으로 따로 빼놓음
necessary = {'a', 'n', 't', 'i', 'c'}
# 입력받은 문자열의 모든 글자에서 necessary를 제외한 글자를 담을 set
other = set()
# 입력받은 문자열에서 necessary를 제외한 나머지 글자
arr = []
for i in range(N):
    # 앞뒤 4글자씩 제외한 문자열에서 중복을 제외하여 necessary 집합에 없는 알파벳만 배열로 모음
    tmp = [j for j in set(list(input().rstrip())[4:-4]) if j not in necessary]
    # other set에 각각의 알파벳을 입력
    other.update(tmp)
    # tmp를 arr에 추가
    arr.append(tmp)
# 이때 K는 5 이상이어야 하기때문에 5 미만일 경우 0을 출력 끗
if K < 5:
    print(0)
else:
    # 필수 알파벳 5개를 제외한 K
    K -= 5
    # arr의 요소들의 bit 합을 저장할 배열
    bit_lst = []
    for i in arr:
        bit = 0
        for j in i:
            # 비트 마스크를 통해 원소 추가
            bit |= 1 << (ord(j) - 97)
        # 모든 원소를 더한 값을 bit_lst에 추가
        bit_lst.append(bit)

    # other 집합에 있는 요소들을 중 통해 K개를 선택한 조합을 생성
    combi = cb(other, min(K, len(other)))
    max_v = 0
    # 조합을 순회
    for i in combi:
        cnt = 0
        bit = 0
        # 현재 조합을 비트 마스크를 통해 원소 추가
        for alp in i:
            bit |= 1 << (ord(alp) - 97)
        # bit_list를 순회하며 현재 조합과 일치하는 요소가 있을 경우 cnt를 1 증가
        for j in bit_lst:
            if bit & j == j:
                cnt += 1
        max_v = max(max_v, cnt)
    print(max_v)


'''
3 6
antarctica
antahellotica
antacartica

rc
hello
car
'''

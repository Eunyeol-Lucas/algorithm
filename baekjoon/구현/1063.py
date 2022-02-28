K, S, N = input().split()

arr = [input() for _ in range(int(N))]
# 입력받은 킹과 스톤의 위치를 열과 행으로 분리시킨 뒤, 열은 아스키 변환으로 숫자로 변경
k_pos = [ord(K[0]), int(K[1])]
s_pos = [ord(S[0]), int(S[1])]
# 명령어에 따른 좌표의 움직임을 담은 딕셔너리
dict = {"R": (1, 0), "L": (-1, 0), "B": (0, -1), "T": (0, 1),
        "RT": (1, 1), "LT": (-1, 1), "RB": (1, -1), "LB": (-1, -1)}

for i in range(int(N)):
    k1, k2 = k_pos[0] + dict[arr[i]][0], k_pos[1] + dict[arr[i]][1]
    # 킹이 명령어를 통해 이동한 위치가 이동 가능한 위치인지 확인
    if 65 <= k1 <= 72 and 1 <= k2 <= 8:
        # 이동한 위치가 현재 스톤의 위치와 겹칠 경우
        if k1 == s_pos[0] and k2 == s_pos[1]:
            s1, s2 = s_pos[0] + dict[arr[i]][0], s_pos[1] + dict[arr[i]][1]
            # 스톤 또한 이동 가능한 위치인지 확인 후 스톤이 이동가능한 범위인 경우 킹과 스톤 모두 이동
            if 65 <= s1 <= 72 and 1 <= s2 <= 8:
                k_pos[0] = k1
                k_pos[1] = k2
                s_pos[0] = s1
                s_pos[1] = s2
        # 킹이 스톤과 인접하지 않은 경우, 킹만 이동
        else:
            k_pos[0] = k1
            k_pos[1] = k2
for i in (k_pos, s_pos):
    print(chr(i[0]) + str(i[1]))


'''
C1 A1 1
L
'''


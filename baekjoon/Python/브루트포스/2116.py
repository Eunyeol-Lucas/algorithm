import sys
input = sys.stdin.readline


def solution(n):
    # 최대값 저장 상수 선언
    answer = 0
    # 첫 번째 주사위 배열 순회
    for i in range(6):
        # 주사위마다 옆면 최대 값을 저장해둘 배열 선언
        result = []
        tmp = [1, 2, 3, 4, 5, 6]
        # 주사위 아랫면을 선택하여 주사위 숫자 배열에서 제거
        tmp.remove(dice_list[0][i])
        # 주사위 아랫면에 따른 윗면을 걔산
        up = dice_list[0][rotate[i]]
        # 첫 번째 주사위에서 윗면 값 제거
        tmp.remove(up)
        # 옆 면의 최대 값 저장
        result.append(max(tmp))
        # 2번째부터 나머지 주사위 배열 순회
        for j in range(1, n):
            tmp = [1, 2, 3, 4, 5, 6]
            # 다음 주사위의 아랫면 숫자 제거
            tmp.remove(up)
            # 다음 주사위의 윗면 값 계산
            up = dice_list[j][rotate[dice_list[j].index(up)]]
            # 윗면 값을 제거
            tmp.remove(up)
            # 옆면의 최대값을 배열에 저장
            result.append(max(tmp))
        # result 배열의 합을 구함
        total = sum(result)

        # 첫 번째 주사위의 아랫면에 따른 전체 값이 더 큰 값을 answer에 저장
        if total > answer:
            answer = total
    return answer


n = int(input())
dice_list = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    dice_list.append(tmp)
# 주사위 아랫면에 따른 윗면의 인덱스 딕셔너리
rotate = {0: 5, 1: 3,
          2: 4, 3: 1, 4: 2, 5: 0}
print(solution(n))

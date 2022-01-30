import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 입력 받은 문자열을 뒤집고 공백을 기준으로 쪼개어 저장
    sentence = input()[::-1].split()
    # 배열을 역순으로 저장
    sentence.reverse()
    # 뛰어쓰기를 기준으로 요소를 구분하여 출력
    print(' '.join(sentence))

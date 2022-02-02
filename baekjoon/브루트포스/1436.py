n = int(input())
six_3 = 666
cnt = 0

while True:
    if '666' in str(six_3):
        cnt += 1
    if cnt == n:
        print(six_3)
        break
    six_3 += 1
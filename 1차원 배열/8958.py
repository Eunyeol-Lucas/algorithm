num = int(input())

for i in range(num):
    OX = input()
    score = 0
    sumScore = 0
    for j in OX:
        if j == "O":
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)
        
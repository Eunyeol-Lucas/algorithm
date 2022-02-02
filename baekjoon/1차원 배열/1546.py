count = int(input())
score = list(map(int, input().split()))
MaxS = max(score)
sum = 0
for i in range(count) :
    Subject = score[i]/MaxS*100
    sum += Subject

print(sum/count)
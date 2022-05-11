num = int(input())
input_num = list(map(int, input()))
sum = 0
for i in range(num):
    sum += input_num[i]
print(sum)

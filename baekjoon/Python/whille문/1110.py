num = int(input())
sum = num
count = 0

while True:
    a = sum//10
    b = sum%10
    c = (a+b) % 10
    sum = (b*10) +c
    count += 1
    if(sum == num):
        break
    
print(count)
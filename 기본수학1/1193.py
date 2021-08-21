N = int(input())
cnt = 1

while N > int(cnt*(cnt+1)/2):
    cnt += 1
    
location = N - cnt*(cnt-1)/2

num1 = str(int(location))
num2 = str(int(cnt - location + 1))

if cnt%2 ==0:
    print(num1+"/"+num2)
else:
    print(num2+'/'+num1)
Arr= []
for i in range(10):
    num = int(input())
    Arr.append(num % 42)

newArr = set(Arr)
print(len(newArr))
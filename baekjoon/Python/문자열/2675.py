import sys 

num = int(sys.stdin.readline())

for i in range(num):
    repeat, alp = sys.stdin.readline().split()
    text = ""
    for j in alp:
        text += int(repeat)*j
    print(text)
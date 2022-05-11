import sys

n = sys.stdin.readline()

answer = ""
for i in range(len(n)):
    if n[i].isalpha():
        if ord(n[i]) + 13 > 122:
            answer += chr(ord(n[i]) - 13)
        elif ord(n[i])+13 > 90 and ord(n[i]) < 91:
            answer += chr(ord(n[i]) - 13)
        else:
            answer += chr(ord(n[i]) + 13)
    else:
        answer += n[i]

print(answer)

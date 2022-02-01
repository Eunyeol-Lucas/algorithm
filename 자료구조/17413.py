import sys
input = sys.stdin.readline

stack = ""
ans = ""
flag = False
words = input().strip()
for i in words:
    if i == "<":
        flag = True
        ans += stack[::-1]
        stack = ""
        ans += i
        continue
    elif i == ">":
        flag = False
        ans += i
        continue
    elif i == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue

    if flag:
        ans += i
    else:
        stack += i

ans+=stack[::-1]  
print(ans)

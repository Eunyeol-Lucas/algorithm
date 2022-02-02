import sys

word = sys.stdin.readline().strip()
answer = [-1]*26
for i in range(len(word)):
    if answer[ord(word[i]) - 97] == -1:
        answer[ord(word[i]) - 97] = i
print(*answer)

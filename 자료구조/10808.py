
import string
'''
input = sys.stdin.readline
answer = [0] * 26
word = input()
alphabet_list = list(string.ascii_lowercase)

dict = {}
for i in word:
    dict.setdefault(i, 0)
    dict[i] += 1
for i in range(26):
    if dict.get(alphabet_list[i]):
        answer[i] = dict.get(alphabet_list[i])
print(*answer)
'''
import sys

answer = [0] * 26
word = sys.stdin.readline().strip()
for i in word:
    answer[ord(i)-97] += 1
print(*answer)

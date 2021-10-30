import sys
from collections import defaultdict

input = sys.stdin.readline

while True:
    word = input().rstrip()
    if word == "*":
        break
    flag = 1
    for i in range(1, len(word)):
        _dict = defaultdict(int)
        for j in range(len(word)-i):
            _dict[word[j]+word[j+i]] += 1
            if _dict[word[j]+word[j+i]] >= 2:
                flag = 0
                break

    print(word, "is surprising.") if flag else print(word, "is NOT surprising.")
import sys

input = sys.stdin.readline

while True:
    word = input().rstrip()
    if word == "*":
        break
    flag = True
    for i in range(1, len(word)):
        _list = []
        for j in range(len(word)-i):
            _list.append(word[j]+word[j+i])
        for k in range(len(_list) -1):
            if _list[k] in _list[k+1:]:
                flag = False

    print(word, "is surprising.") if flag else print(word, "is NOT surprising.")
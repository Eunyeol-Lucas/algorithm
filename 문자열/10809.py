import string
word = input()
alp = string.ascii_lowercase

for i in alp:
    print(word.find(i), end=' ')

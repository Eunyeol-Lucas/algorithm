import string
word = input()
alphabet = string.ascii_lowercase

for i in alphabet:
    print(word.find(i), end=' ')

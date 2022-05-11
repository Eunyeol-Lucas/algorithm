a = 0

for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        a += 1

print(a)
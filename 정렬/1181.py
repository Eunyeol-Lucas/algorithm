
result = []
for i in range(int(input())):
    word = input()
    result.append(word)

word_list = (sorted(sorted(set(result)), key=len))

for i in word_list:
    print(i)
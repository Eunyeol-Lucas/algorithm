word = input()

if "A" in word:
    word = word.replace('B','A').replace('C','A').replace('D','A').replace("F",'A')
elif "B" in word:
    word = word.replace('C','B').replace('D','B').replace('F','B')
elif "C" in word:
    word = word.replace('D','C').replace('F','C')
else:
    word = 'A'*len(word)
print(word)


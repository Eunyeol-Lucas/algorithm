dict = ["c=", "c-","dz=","d-","lj","nj","s=","z="]
word = input()

for i in dict:
    word = word.replace(i, "_")
print(len(word))
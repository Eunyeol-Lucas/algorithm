num = int(input())
cnt = 0

for i in range(num):
    word = input()
    word_list = [word[0]]
    error = 0
    if len(word) == 1:
        cnt += 1
    else:
        for  j in range(1, len(word)):
            if word[j-1] != word[j]:
                word_list.append(word[j]) 
        
            if word[j] in word_list[:-1]:
                 error += 1

        if error == 0:
            cnt += 1
    
print(cnt)
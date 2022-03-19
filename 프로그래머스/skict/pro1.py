def solution(goods):
    answer = [[] for _ in range(len(goods))]
    max_len = 0
    for i in goods:
        max_len = max(max_len, len(i))
    for i in range(1, max_len+1):
        n_tmp = []
        for j in range(len(goods)):
            if answer[j] == [] and len(goods[j]) >= i:
                for k in range(0, len(goods[j])+1-i):
                    alp = goods[j][k:k+i]
                    flag = 0
                    for o in range(len(goods)):
                        if o != j:
                            if goods[o].find(alp) != -1 and alp not in n_tmp:
                                flag = 1
                                n_tmp.append(alp)
                                break
                    if flag == 0 and alp not in answer[j] and alp not in n_tmp:
                        answer[j].append(alp)

    for i in range(len(goods)):
        answer[i].sort()
        if answer[i] != []:
            tmp = " ".join(answer[i])
        else:
            tmp = "None"
        answer[i] = tmp

    return answer


goods = ["cd", "dd", "abcdabcd", "abcdabcdabcdabcd"]
# goods = ["abcdeabcd", "abcddeabcx", "abcdeabcda", "abcdeabcy"]
# goods = ["pencil", "cilicon", "contrabase", "picturelist"]
print(solution(goods))

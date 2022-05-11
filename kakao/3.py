def solution(alp, cop, problems):
    answer = 0
    vst = [0] * len(problems)
    for i in range(len(problems)):
        if problems[i][0] <= alp and problems[i][1] <= cop:
            alp += problems[i][2]
            cop += problems[i][3]
            answer += problems[i][4]
            vst[i] = 1
    
    return answer


a = 0
c = 0
p = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]
print(solution(a, c, p))

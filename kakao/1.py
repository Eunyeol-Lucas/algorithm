def solution(survey, choices):
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        a, b = list(survey[i])
        if choices[i] > 4:
            dict[b] += choices[i] - 4
        else:
            dict[a] += 4 - choices[i]
    answer = ''
    for a, b in (('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')):
        answer += a if dict[a] >= dict[b] else b
    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))

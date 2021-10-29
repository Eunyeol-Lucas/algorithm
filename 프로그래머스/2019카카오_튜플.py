from collections import Counter

def solution(s):
    _list = s.replace('{', '').replace('}', '').split(',')
    result = Counter(_list).most_common()
    return [int(num) for num, _ in result]
def solution(record):
    _dict = {}
    answer = []
    
    for rec in record:
        recs = rec.split()
        if recs[0] == "Enter":
            _dict[recs[1]] = recs[2]
            answer.append((recs[1], '님이 들어왔습니다.'))
        elif recs[0] == "Leave":
            answer.append((recs[1], '님이 나갔습니다.'))
        else:
            _dict[recs[1]] = recs[2]
    
    return [_dict[dt[0]] + dt[1] for dt in answer]
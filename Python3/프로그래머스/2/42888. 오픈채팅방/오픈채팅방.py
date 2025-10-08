def solution(record):
    answer = []
    name = {}
    for r in record:
        r = r.split(' ')
        if r[0] != 'Leave':
            name[r[1]] = r[2]
            
    for r in record:
        r = r.split(' ')
        if r[0] == 'Enter':
            answer.append(name[r[1]] + '님이 들어왔습니다.')
        if r[0] == 'Leave':
            answer.append(name[r[1]] + '님이 나갔습니다.')
    return answer

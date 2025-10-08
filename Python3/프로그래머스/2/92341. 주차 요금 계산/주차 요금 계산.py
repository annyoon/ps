import math

def convert(time):
    t = time.split(':')
    return int(t[0]) * 60 + int(t[1])

def getFees(m, fees):
    if m <= fees[0]:
        return fees[1]
    return fees[1] + math.ceil((m - fees[0]) / fees[2]) * fees[3]

def solution(fees, records):
    result = {}
    dic = {}
    for record in records:
        r = record.split(' ')
        if r[2] == 'IN':
            dic[r[1]] = convert(r[0])
        else:
            m = convert(r[0]) - dic[r[1]]
            if r[1] in result:
                result[r[1]] += m
            else:
                result[r[1]] = m
            dic[r[1]] = -1
    for d in dic.items():
        if d[1] != -1:
            m = convert('23:59') - d[1]
            if d[0] in result:
                result[d[0]] += m
            else:
                result[d[0]] = m
    return [getFees(r[1], fees) for r in sorted(result.items(), key = lambda x: x[0])]

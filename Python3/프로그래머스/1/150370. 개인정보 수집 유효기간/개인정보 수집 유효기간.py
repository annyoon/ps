def getDays(y, m, d):
    return (int(y) - 2000) * 12 * 28 + (int(m) - 1) * 28 + int(d) - 1

def solution(today, terms, privacies):
    dic = {}
    for term in terms:
        t = term.split(' ')
        dic[t[0]] = int(t[1]) * 28 - 1
    
    t = today.split('.')
    days = getDays(t[0], t[1], t[2])
    
    answer = []
    for i in range(len(privacies)):
        p = privacies[i].split(' ')
        dates, term = p[0].split('.'), p[1]
        pDays = getDays(dates[0], dates[1], dates[2])
        if pDays + dic[term] < days:
            answer.append(i + 1)
            
    return answer

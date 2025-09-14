def solution(s):
    answer = ''
    isFirst = True
    for w in s:
        if w != ' ':
            if isFirst:
                answer += w.upper()
                isFirst = False
            else:
                answer += w.lower()
        else:
            isFirst = True
            answer += w
    return answer

def solution(s):
    answer = 0
    same, diff = 1, 0
    x = ''
    for c in s:
        if x == '':
            x = c
        else:
            if c == x:
                same += 1
            if c != x:
                diff += 1
        if same == diff:
            answer += 1
            same, diff = 1, 0
            x = ''
    if x != '':
        answer += 1
    return answer

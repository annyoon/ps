def solution(new_id):
    new_id = new_id.lower()
    
    answer = ''
    for i in new_id:
        if i.isalnum() or i == '-' or i == '_':
            answer += i
        elif i == '.':
            if len(answer) < 1 or answer[-1] != '.':
                answer += i
    answer = answer.strip('.')
    
    if answer == '':
        answer = 'a'
    elif len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')
        
    if len(answer) <= 2:
        c = answer[-1]
        while len(answer) < 3:
            answer += c
            
    return answer

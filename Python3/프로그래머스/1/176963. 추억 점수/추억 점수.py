def solution(name, yearning, photo):
    dic, answer = {}, []
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    for p in photo:
        acc = 0
        for key in p:
            if key in dic:
                acc += dic[key]
        answer.append(acc)
        
    return answer

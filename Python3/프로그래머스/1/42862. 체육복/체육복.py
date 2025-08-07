def solution(n, lost, reserve):
    lostSet, reserveSet = set(lost), set(reserve)
    s = lostSet & reserveSet
    lostSet -= s
    reserveSet -= s
    
    answer = n - len(lostSet)
    dic = {}
    
    for l in lostSet:
        dic[l] = True
        
    for r in reserveSet:
        if r - 1 in dic and dic[r - 1]:
            dic[r - 1] = False
            answer += 1
        elif r + 1 in dic and dic[r + 1]:
            dic[r + 1] = False
            answer += 1
            
    return answer

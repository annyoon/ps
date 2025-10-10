def solution(gems):
    answer = [1, len(gems)]
    l = len(set(gems))
    dic = {}
    start, end = 0, 0
    
    while end < len(gems):
        gem = gems[end]
        dic[gem] = dic.get(gem, 0) + 1
        while len(dic) == l:
            if answer[1] - answer[0] > end - start:
                answer = [start + 1, end + 1]
            if start < end:
                dic[gems[start]] -= 1
                if dic[gems[start]] == 0:
                    del dic[gems[start]]
                start += 1
            else:
                break
        end += 1
        
    return answer

def solution(k, tangerine):
    answer = 0
    dic = {}
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
    arr = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    count = 0
    for a in arr:
        answer += 1
        count += a[1]
        if count >= k:
            break
    return answer

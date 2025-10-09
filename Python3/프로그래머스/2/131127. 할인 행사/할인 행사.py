def check(want, number, dic):
    for i in range(len(want)):
        if want[i] not in dic or dic[want[i]] < number[i]:
            return False
    return True

def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(10):
        if discount[i] in dic:
            dic[discount[i]] += 1
        else:
            dic[discount[i]] = 1
    if check(want, number, dic):
        answer += 1
    start, end = 0, 10
    while end < len(discount):
        dic[discount[start]] -= 1
        if discount[end] in dic:
            dic[discount[end]] += 1
        else:
            dic[discount[end]] = 1
        if check(want, number, dic):
            answer += 1
        start += 1
        end += 1
    return answer

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    dic = {}
    dq = deque()
    for city in cities:
        city = city.lower()
        if city in dic and dic[city]:
            answer += 1
            for _ in range(len(dq)):
                p = dq.popleft()
                if p != city:
                    dq.append(p)
        else:
            answer += 5
        if cacheSize > 0:
            if len(dq) == cacheSize:
                p = dq.popleft()
                dic[p] = False
            dq.append(city)
            dic[city] = True
    return answer

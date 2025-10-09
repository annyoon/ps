from collections import deque

def solution(queue1, queue2):
    answer = 0
    s1, s2 = sum(queue1), sum(queue2)
    if (s1 + s2) % 2 == 1:
        return -1
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    
    while s1 != s2:
        if answer > (len(queue1) + len(queue2)) * 2:
            return -1
        if s1 > s2:
            p = dq1.popleft()
            dq2.append(p)
            s1 -= p
            s2 += p
        else:
            p = dq2.popleft()
            dq1.append(p)
            s2 -= p
            s1 += p
        answer += 1
    return answer

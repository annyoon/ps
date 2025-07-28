from collections import deque

def solution(cards1, cards2, goal):
    c1, c2 = deque(cards1), deque(cards2)
    
    for g in goal:
        if len(c1) > 0 and c1[0] == g:
            c1.popleft()
            continue
        if len(c2) > 0 and c2[0] == g:
            c2.popleft()
            continue
        return "No"
    return "Yes"

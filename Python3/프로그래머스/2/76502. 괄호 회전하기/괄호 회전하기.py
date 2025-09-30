from collections import deque

def check(dq):
    arr = []
    for d in dq:
        arr.append(d)
        if len(arr) > 1:
            if (arr[-2] == "(" and arr[-1] == ")") or (arr[-2] == "{" and arr[-1] == "}") or (arr[-2] == "[" and arr[-1] == "]"):
                arr.pop()
                arr.pop()
    if len(arr) > 0:
        return False
    return True

def solution(s):
    answer = 0
    dq = deque(s)
    for _ in range(len(s)):
        if check(dq):
            answer += 1
        left = dq.popleft()
        dq.append(left)
    
    return answer

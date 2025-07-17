def solution(a, b):
    answer = 0
    start = a if a <= b else b
    end = a if a > b else b
    
    for i in range(start, end + 1):
        answer += i
    return answer

def solution(arr):
    answer = []
    prev = -1
    for a in arr:
        if a != prev:
            answer.append(a)
        prev = a
    return answer

def solution(n, m, section):
    answer, cur = 0, 0
    for s in section:
        if s > cur:
            cur = s + m - 1
            answer += 1
    return answer

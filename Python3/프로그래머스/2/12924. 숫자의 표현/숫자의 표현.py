def solution(n):
    if n == 1:
        return 1
    answer = 0
    num = 1
    start, end = 1, 2
    while start < end or end <= n:
        if num < n:
            num += end
            end += 1
        elif num == n:
            answer += 1
            num -= start
            start += 1
        elif num > n:
            num -= start
            start += 1
    return answer

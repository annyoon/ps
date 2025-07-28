def getDivisor(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += 1
            if i ** 2 != n:
                answer += 1
    return answer
    
def solution(number, limit, power):
    answer = 0
    for n in range(1, number + 1):
        p = getDivisor(n)
        if p <= limit:
            answer += p
        else:
            answer += power
    return answer

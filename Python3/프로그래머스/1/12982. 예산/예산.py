def solution(d, budget):
    answer, acc = 0, 0
    for money in sorted(d):
        acc += money
        if acc > budget:
            return answer
        answer += 1
    return answer

def getDivisorCount(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if i ** 2 != n:
                count += 1
    return 1 if count % 2 == 0 else -1

def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        answer += getDivisorCount(n) * n
    return answer

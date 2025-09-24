def solution(n,a,b):
    answer = 1
    while min(a, b) % 2 == 0 or min(a, b) + 1 != max(a, b):
        answer += 1
        if a % 2 == 0:
            a = a // 2
        else:
            a = (a + 1) // 2
        if b % 2 == 0:
            b = b // 2
        else:
            b = (b + 1) // 2
    return answer

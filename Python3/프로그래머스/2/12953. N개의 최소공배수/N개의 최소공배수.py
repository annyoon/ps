import math

def solution(arr):
    answer = 1
    for a in arr:
        answer = answer * a // math.gcd(answer, a)
    return answer

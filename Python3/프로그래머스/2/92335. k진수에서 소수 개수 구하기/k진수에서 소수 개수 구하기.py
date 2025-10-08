def convert(n, k):
    base = ''
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)
    return base[::-1]

def isPrimeNumber(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    arr = convert(n, k).split('0')
    for a in arr:
        if a.isdigit() and isPrimeNumber(int(a)):
            answer += 1
    return answer

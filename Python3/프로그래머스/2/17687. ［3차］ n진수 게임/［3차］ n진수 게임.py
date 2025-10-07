digits = "0123456789ABCDEF"

def solve(n, q):
    base = ''
    while n > 0:
        n, mod = divmod(n, q)
        base += digits[mod]
    return base[::-1]

def solution(n, t, m, p):
    answer = ''
    string = '0'
    i = 1
    while len(string) < t * m:
        string += solve(i, n)
        i += 1
    for j in range(p - 1, t * m, m):
        answer += string[j]
    return answer

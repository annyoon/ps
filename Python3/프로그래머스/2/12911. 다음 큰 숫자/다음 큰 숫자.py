def solution(n):
    cn = bin(n).count('1')
    cur = n + 1
    c = bin(cur).count('1')
    while cn != c:
        cur += 1
        c = bin(cur).count('1')
    return cur

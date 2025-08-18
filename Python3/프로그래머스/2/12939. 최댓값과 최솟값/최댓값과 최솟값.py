def solution(s):
    s = [int(c) for c in s.split()]
    return str(min(s)) + ' ' + str(max(s))

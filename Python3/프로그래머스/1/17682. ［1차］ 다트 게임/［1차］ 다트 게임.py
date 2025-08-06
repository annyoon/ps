def solution(dartResult):
    arr = []
    cur = 0
    flag = False
    for c in dartResult:
        if c.isdigit():
            if flag or len(arr) == 0:
                arr.append(cur)
                cur = int(c)
                flag = False
            else:
                cur = 10
        else:
            flag = True
            if c == 'D':
                cur = cur ** 2
            elif c == 'T':
                cur = cur ** 3
            elif c == '*':
                arr[-1] = arr[-1] * 2
                cur *= 2
            elif c == '#':
                cur = 0 - cur
    return sum(arr) + cur

def getHeadNum(string):
    h, n = '', ''
    for s in string:
        if len(n) == 5 or (len(n) > 0 and not s.isdigit()):
            break
        if s.isdigit():
            n += s
        else:
            h += s
    return [h, n]

def solution(files):
    def sortKey(x):
        h, n = getHeadNum(x)
        return (h.lower(), int(n))

    return sorted(files, key = sortKey)

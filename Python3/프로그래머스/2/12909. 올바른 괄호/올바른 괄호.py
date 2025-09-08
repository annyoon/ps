def solution(s):
    cl, cr = 0, 0
    for c in s:
        if c == "(":
            cl += 1
        if c == ")":
            cr += 1
        if cr > cl:
            return False
    if cl != cr:
        return False
    return True

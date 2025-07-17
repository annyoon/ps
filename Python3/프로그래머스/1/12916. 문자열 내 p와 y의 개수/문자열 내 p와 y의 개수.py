def solution(s):
    pNum, yNum = 0, 0
    for c in s:
        if c == 'p' or c == 'P':
            pNum += 1
        elif c == 'y' or c == 'Y':
            yNum += 1
    return pNum == yNum

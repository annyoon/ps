def solution(s):
    answer = [0, 0]
    while s != '1':
        z = s.count('0')
        d = len(s) - z
        s = bin(int(d))[2:]
        answer[0] += 1
        answer[1] += z
    return answer

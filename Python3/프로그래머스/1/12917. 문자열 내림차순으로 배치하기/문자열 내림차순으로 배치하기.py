def solution(s):
    answer = ''
    for n in sorted([ord(c) for c in s], reverse = True):
        answer += chr(n)
    return answer

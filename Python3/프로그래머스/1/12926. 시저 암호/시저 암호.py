def solution(s, n):
    answer = ''
    for a in s:
        if 'A' <= a <= 'Z':
            next = ord(a) + n 
            answer += chr(next) if next <= ord('Z') else chr(next - ord('Z') + ord('A') - 1)
        elif 'a' <= a <= 'z':
            next = ord(a) + n 
            answer += chr(next) if next <= ord('z') else chr(next - ord('z') + ord('a') - 1)
        else:
            answer += a
    return answer

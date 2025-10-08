def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        a = ord('A') + i
        dic[chr(a)] = i + 1
    
    def solve(w, index, num):
        if index + 1 >= len(msg):
            answer.append(dic[w])
            return
        answer.append(dic[w])
        c = msg[index + 1]
        dic[w + c] = num
        ni = index + 1
        for i in range(index + 2, len(msg)):
            if c + msg[i] not in dic:
                break
            c += msg[i]
            ni = i
        solve(c, ni, num + 1)
        
    solve(msg[0], 0, 27)
    return answer

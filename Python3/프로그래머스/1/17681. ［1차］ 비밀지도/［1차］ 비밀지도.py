def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        s = ""
        code1, code2 = bin(arr1[i])[2:].zfill(n), bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if code1[j] == "1" or code2[j] == "1":
                s += '#'
            else:
                s += " "
        answer.append(s)
    return answer

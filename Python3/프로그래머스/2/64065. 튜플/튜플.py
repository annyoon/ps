def solution(s):
    answer = []
    sArr, arr = [], []
    string = ''
    for i in range(1, len(s) - 1):
        if s[i].isdigit():
            string += s[i]
        if s[i] == ',' and len(string):
            arr.append(int(string))
            string = ''
        if s[i] == '}':
            arr.append(int(string))
            string = ''
            sArr.append(arr)
            arr = []
    sArr = sorted(sArr, key = lambda x: len(x))
    
    dic = {}
    for a in sArr:
        for num in a:
            if num not in dic:
                answer.append(num)
                dic[num] = True
    return answer

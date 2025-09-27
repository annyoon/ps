def solution(elements):
    dic = {}
    for i in range(len(elements)):
        arr = elements + elements[:i]
        num = sum(elements[:i + 1])
        if num not in dic:
                dic[num] = True
        for j in range(len(elements) - 1):
            num = num - arr[j] + arr[i + j + 1]
            if num not in dic:
                dic[num] = True
    return len(dic)

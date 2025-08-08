def solution(ingredient):
    answer = 0
    arr = []
    for i in ingredient:
        arr.append(str(i))
        if len(arr) >= 4:
            if ''.join(arr[-1:-5:-1]) == '1321':
                for j in range(4):
                    arr.pop()
                answer += 1
    return answer

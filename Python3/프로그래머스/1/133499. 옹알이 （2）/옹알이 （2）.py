def solution(babbling):
    answer = 0
    arr1 = ["ayaaya", "yeye", "woowoo", "mama"]
    arr2 = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        flag = False
        for a in arr1:
            if a in b:
                flag = True
                break
        if not flag:
            for a in arr2:
                b = b.replace(a, " ")
                if b.strip() == "":
                    answer += 1
                    break
    return answer

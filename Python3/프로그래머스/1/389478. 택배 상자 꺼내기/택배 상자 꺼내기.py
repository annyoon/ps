def solution(n, w, num):
    total, find = [], []
    box, reverse = 1, False
    floor = n // w if n % w == 0 else n // w + 1
    
    for i in range(floor):
        arr = []
        for j in range(w):
            if box == num:
                if reverse:
                    find = [i, w - j - 1]
                else:
                    find = [i, j]
            arr.append(box)
            box += 1
        if reverse:
            total.append(arr[::-1])
            reverse = False
        else:
            total.append(arr)
            reverse = True
            
    answer = floor - find[0]
    if total[floor - 1][find[1]] > n:
        answer -= 1
        
    return answer

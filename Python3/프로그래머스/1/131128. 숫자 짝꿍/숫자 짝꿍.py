def solution(X, Y):
    dic = {}
    arr = [0] * 10
    
    for n in X:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
            
    for n in Y:
        if n in dic and dic[n] > 0:
            dic[n] -= 1
            arr[int(n)] += 1
                
    result = ''
    zero = True
    for n in range(9, -1, -1):
        if n != 0 and arr[n] != 0:
            zero = False
        result += (str(n) * arr[n])
        
    if result == '':
        return '-1'
    if zero:
        return '0'
    return result

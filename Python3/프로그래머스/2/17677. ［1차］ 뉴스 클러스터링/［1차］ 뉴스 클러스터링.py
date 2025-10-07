def convert(string):
    arr = []
    for i in range(len(string) - 1):
        if string[i].isalpha() and string[i + 1].isalpha():
            arr.append(string[i].lower() + string[i + 1].lower())
    return arr

def solve(arr):
    dic = {}
    for a in arr:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    return dic
        
def solution(str1, str2):
    arr1, arr2 = convert(str1), convert(str2)
    dic1, dic2 = solve(arr1), solve(arr2)
    dic = {}
    i, u = 0, 0
    
    for a in arr1:
        if a not in dic:
            dic[a] = True
            tmp = dic2[a] if a in dic2 else 0
            i += min(dic1[a], tmp)
            u += max(dic1[a], tmp)
    for a in arr2:
        if a not in dic:
            dic[a] = True
            tmp = dic1[a] if a in dic1 else 0
            i += min(dic2[a], tmp)
            u += max(dic2[a], tmp)
            
    if i == 0 and u == 0:
        return 65536
    return i / u * 65536 // 1

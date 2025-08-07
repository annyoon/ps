def solution(keymap, targets):
    result = []
    dic = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in dic:
                dic[key[i]] = i + 1
            elif i + 1 < dic[key[i]]:
                dic[key[i]] = i + 1
                
    for target in targets:
        count = 0
        for t in target:
            if t not in dic:
                count = -1
                break
            count += dic[t]
        result.append(count)
    return result

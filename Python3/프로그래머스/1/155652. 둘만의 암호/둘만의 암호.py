def solution(s, skip, index):
    result, arr = '', []
    for c in skip:
        arr.append(ord(c))
    for c in s:
        nxt = ord(c)
        i = 0
        while i < index:
            nxt = nxt + 1 if nxt < ord('z') else ord('a')
            if nxt in arr:
                i -= 1
            i += 1
        result += chr(nxt)
    return result

def solution(s):
    arr = []
    for a in s:
        arr.append(a)
        if len(arr) > 1 and arr[-1] == arr[-2]:
            arr.pop()
            arr.pop()
    if len(arr) == 0:
        return 1
    return 0

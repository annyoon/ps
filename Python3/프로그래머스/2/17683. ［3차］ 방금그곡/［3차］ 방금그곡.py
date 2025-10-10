def convert(time):
    t = time.split(':')
    return int(t[0]) * 60 + int(t[1])

def solution(m, musicinfos):
    mArr = []
    for c in m:
        if c != '#':
            mArr.append(c)
        else:
            mArr[-1] = mArr[-1] + c
    dic = {}
    for j in range(len(musicinfos)):
        info = musicinfos[j]
        time1, time2, name, code = info.split(',')
        minute = convert(time2) - convert(time1)
        arr = []
        i = 0
        while len(arr) < minute:
            c = code[i % len(code)]
            if c != '#':
                arr.append(c)
            else:
                arr[-1] = arr[-1] + c
            i += 1
        c = code[i % len(code)]
        if c == '#':
            arr[-1] = arr[-1] + c
        idx = 0
        for a in arr:
            if a == mArr[idx]:
                if idx == len(mArr) - 1:
                    dic[name] = [minute, len(musicinfos) - j]
                    break
                idx += 1
            else:
                idx = 0
                if a == mArr[idx]:
                    idx += 1
    if len(dic) == 0:
        return '(None)'
    if len(dic) == 1:
        return list(dic)[0]
    d = sorted(dic.items(), key = lambda x: (x[1][0], x[1][1]), reverse = True)
    return d[0][0]

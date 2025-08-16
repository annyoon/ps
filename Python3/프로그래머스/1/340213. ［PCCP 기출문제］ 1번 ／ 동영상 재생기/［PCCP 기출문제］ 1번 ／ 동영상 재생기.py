def getSec(time):
    arr = time.split(':')
    return int(arr[0]) * 60 + int(arr[1])

def solution(video_len, pos, op_start, op_end, commands):
    total = getSec(video_len)
    pos = getSec(pos)
    start, end = getSec(op_start), getSec(op_end)
    
    for command in commands:
        if start <= pos <= end:
            pos = end
        if command == 'next':
            nPos = pos + 10
            pos = min(nPos, total)
        if command == 'prev':
            nPos = pos - 10
            pos = max(nPos, 0)
    
    if start <= pos <= end:
        pos = end
    
    minute = str(pos // 60)
    sec = str(pos % 60)
    
    while len(minute) < 2:
        minute = '0' + minute
        
    while len(sec) < 2:
        sec = '0' + sec

    return minute + ':' + sec

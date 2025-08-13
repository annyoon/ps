def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        end = schedules[i] + 10
        end = end if end % 100 < 60 else end // 100 * 100 + 100 + end % 100 - 60
        isLate = False
        
        for j in range(7):
            log = timelogs[i][j]
            day = startday + j
            if day % 7 == 0 or day % 7 == 6:
                continue
            if log > end:
                isLate = True
                break
                
        if not isLate:
            answer += 1
            
    return answer

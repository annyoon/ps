def solution(id_list, report, k):
    count, dic, result = {}, {}, {}
    
    for id in id_list:
        count[id] = 0
        result[id] = 0
        
    for r in report:
        r = r.split()
        reporter, reported = r[0], r[1]
        if reporter in dic:
            if reported in dic[reporter]:
                continue
            dic[reporter][reported] = True
        else:
            dic[reporter] = {}
            dic[reporter][reported] = True
        count[reported] += 1
        
    for reported in count:
        if count[reported] >= k:
            for reporter in result:
                if reporter in dic and reported in dic[reporter]:
                    result[reporter] += 1
                    
    return list(result.values())

def solution(lottos, win_nums):
    count = 0
    for num in win_nums:
        if num in lottos:
            count += 1
    total = count + lottos.count(0)
    maxRank = 7 - total if total != 0 else 6
    minRank = 7 - count if count != 0 else 6
    return [maxRank, minRank]

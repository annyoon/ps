def solution(k, score):
    answer = []
    rank = []
    for s in score:
        if len(rank) < k:
            rank.append(s)
        else:
            m = min(rank)
            if s > m:
                rank.remove(m)
                rank.append(s)
        answer.append(min(rank))
    return answer

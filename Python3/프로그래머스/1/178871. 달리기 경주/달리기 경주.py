def solution(players, callings):
    ranks, names = {}, {}
    
    for i in range(len(players)):
        names[i] = players[i]
        ranks[players[i]] = i
        
    for palyer in callings:
        rank = ranks[palyer]
        nextPlayer = names[rank - 1]
        
        ranks[palyer] -= 1
        ranks[nextPlayer] += 1
        
        names[rank - 1] = palyer
        names[rank] = nextPlayer
        
    return list(names.values())

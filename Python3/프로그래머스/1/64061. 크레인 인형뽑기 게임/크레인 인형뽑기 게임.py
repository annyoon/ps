def solution(board, moves):
    count = 0
    basket = []
    
    for move in moves:
        for d in range(len(board)):
            if board[d][move - 1] != 0:
                basket.append(board[d][move - 1])
                board[d][move - 1] = 0
                break
        if len(basket) >= 2:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                count += 2
                
    return count

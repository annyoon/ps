def inRange(h, w, n):
    return 0 <= h < n and 0 <= w < n

def solution(board, h, w):
    answer = 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(4):
        nh, nw = h + dx[i], w + dy[i]
        if inRange(nh, nw, len(board)) and board[nh][nw] == board[h][w]:
            answer += 1
    return answer

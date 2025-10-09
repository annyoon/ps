def check(board, cur):
    b = board[cur[0]][cur[1]]
    if b == 0:
        return False
    if b == board[cur[0] + 1][cur[1]] and b == board[cur[0]][cur[1] + 1] and b == board[cur[0] + 1][cur[1] + 1]:
        return True
    return False

def move(board, nBoard, m, n):
    for c in range(n):
        arr = []
        for r in range(m - 1, -1, -1):
            if not nBoard[r][c]:
                arr.append(board[r][c])
        for r in range(m):
            if r >= len(arr):
                board[m - r - 1][c] = 0
            else:
                board[m - r - 1][c] = arr[r]
    return board

def solution(m, n, board):
    answer = 0
    dx, dy = [0, 1, 0, 1], [0, 0, 1, 1]
    for i in range(len(board)):
        board[i] = list(board[i])
    flag = True
    while flag:
        flag = False
        nBoard = [[False] * n for _ in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and check(board, [i, j]):
                    flag = True
                    for d in range(4):
                        nr, nc = i + dx[d], j + dy[d]
                        if not nBoard[nr][nc]:
                            answer += 1
                            nBoard[nr][nc] = True
        board = move(board, nBoard, m, n)
    return answer

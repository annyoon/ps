board = []
dx, dy = [0, 1, 1], [1, 0, 1]

def inRange(r, c):
    global board
    return 0 <= r < len(board) and 0 <= c < len(board[0])

def find(mat, size, num):
    global board
    new = []
    
    for cur in mat: # [r, c]
        for d in range(3):
            nr, nc = cur[0] + dx[d], cur[1] + dy[d]
            if inRange(nr, nc) and not board[nr][nc].isalpha():
                if board[nr][nc] != num:
                    board[nr][nc] = num
                    new.append([nr, nc])
            else:
                return size
    return find(new, size + 1, num)
    

def solution(mats, park):
    global board
    board = park
    maxSize = max(mats)
    size, num = 0, 0
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if not park[i][j].isalpha():
                size = max(size, find([[i, j]], 0, str(num)))
                num += 1
            
                if size + 1 >= maxSize:
                    return maxSize
            
    for mat in sorted(mats, reverse = True):
        if size + 1 >= mat:
            return mat
        
    return -1

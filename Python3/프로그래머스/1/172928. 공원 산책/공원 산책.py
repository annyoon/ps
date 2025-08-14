def inRange(r, c, n, m):
    return 0 <= r < n and 0 <= c < m

def solution(park, routes):
    dic = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}
    flag, cur = False, []
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                flag = True
                cur = [i, j]
                break
        if flag:
            break
            
    for route in routes:
        arr = route.split()
        d, dist = dic[arr[0]], int(arr[1])
        nCur = cur
        
        while dist:
            nr, nc = nCur[0] + d[0], nCur[1] + d[1],
            if inRange(nr, nc, len(park), len(park[0])) and park[nr][nc] != 'X':
                nCur = [nr, nc]
                dist -= 1
            else:
                break
                
        if dist == 0:
            cur = nCur
            
    return cur

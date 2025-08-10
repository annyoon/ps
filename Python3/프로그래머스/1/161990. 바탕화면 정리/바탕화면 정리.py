def solution(wallpaper):
    minH, maxH = len(wallpaper), 0
    minW, maxW = len(wallpaper[0]), 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < minH:
                    minH = i
                if i > maxH:
                    maxH = i
                if j < minW:
                    minW = j
                if j > maxW:
                    maxW = j
                
    return [minH, minW, maxH + 1, maxW + 1]

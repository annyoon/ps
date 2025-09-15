def solution(brown, yellow):
    for h in range(1, int(yellow ** 0.5) + 1):
        if yellow % h == 0:
            w = yellow // h
            bh, bw = h + 2, w + 2
            if bh * 2 + bw * 2 - 4 == brown:
                return [bw, bh]

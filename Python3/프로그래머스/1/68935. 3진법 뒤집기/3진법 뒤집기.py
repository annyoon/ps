def solution(n):
    revBase = ''
    while n > 0:
        n, mod = divmod(n, 3)
        revBase += str(mod)
    return int(revBase, 3)

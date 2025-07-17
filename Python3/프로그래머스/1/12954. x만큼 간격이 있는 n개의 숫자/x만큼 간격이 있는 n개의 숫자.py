def solution(x, n):
    if x == 0:
        return [x] * n
    return [number for number in range(x, x * n, x)] + [x * n]

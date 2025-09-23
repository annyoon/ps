def solution(n):
    arr = [0, 1, 2]
    if n == 1 or n == 2:
        return arr[n]
    for i in range(3, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[n] % 1234567

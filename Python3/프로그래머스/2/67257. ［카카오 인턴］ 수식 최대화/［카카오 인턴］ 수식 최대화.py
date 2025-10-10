from itertools import permutations

def solve(arr, depth, operands):
    if isinstance(arr, str):
        return int(arr)
    result = 0
    if operands[depth] == '+':
        for a in arr:
            result += solve(a, depth + 1, operands)
    elif operands[depth] == '-':
        for i in range(len(arr)):
            a = arr[i]
            if i == 0:
                result += solve(a, depth + 1, operands)
            else:
                result -= solve(a, depth + 1, operands)
    else:
        result = 1
        for a in arr:
            result *= solve(a, depth + 1, operands)
    return result

def solution(expression):
    answer = 0
    for operands in list(permutations(['*', '+', '-'], 3)):
        arr = expression.split(operands[0])
        for i in range(len(arr)):
            arr[i] = arr[i].split(operands[1])
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] = arr[i][j].split(operands[2])
        answer = max(answer, abs(solve(arr, 0, operands)))
    return answer

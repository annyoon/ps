def solution(sizes):
    answer = [0, 0]
    for size in sizes:
        num1 = max(size[0], answer[0]) * max(size[1], answer[1])
        num2 = max(size[0], answer[1]) * max(size[1], answer[0])
        if num1 < num2:
            answer = [max(size[0], answer[0]), max(size[1], answer[1])]
        else:
            answer = [max(size[0], answer[1]), max(size[1], answer[0])]
    return answer[0] * answer[1]

def solution(answers):
    answer = []
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    counts = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == arr1[i % 5]:
            counts[0] += 1
        if answers[i] == arr2[i % 8]:
            counts[1] += 1
        if answers[i] == arr3[i % 10]:
            counts[2] += 1
    
    for i in range(3):
        if counts[i] == max(counts):
            answer.append(i + 1)
    
    return answer

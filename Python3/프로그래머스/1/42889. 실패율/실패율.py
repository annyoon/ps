def solution(N, stages):
    answer = []
    arr = [0] * (N + 1)
    for stage in stages:
        arr[stage - 1] += 1
    
    cur = len(stages)
    for i in range(N):
        if cur == 0:
            answer.append(0)
        else:
            answer.append(arr[i] / cur)
            cur -= arr[i]
        
    answer = sorted(list(enumerate(answer, 1)), key = lambda x: (-x[1], x))
    return [x[0] for x in answer]

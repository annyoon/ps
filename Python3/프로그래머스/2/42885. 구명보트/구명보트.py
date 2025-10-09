def solution(people, limit):
    answer = 0
    people.sort()
    end = len(people) - 1
    for start in range(len(people)):
        if start >= end:
            break
        while start < end:
            answer += 1
            if people[start] + people[end] > limit:
                end -= 1
                if end == start:
                    answer += 1
            else:
                end -= 1
                if end - 1 == start:
                    answer += 1
                break
    return answer

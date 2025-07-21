from itertools import combinations

def solution(numbers):
    return sorted(list(set([sum(combi) for combi in list(combinations(numbers, 2))])))

from itertools import combinations

def solution(orders, course):
    dic = {}
    mx = {}
    for c in course:
        mx[c] = 1
    for order in orders:
        for c in course:
            for comb in list(combinations(order, c)):
                num = 1
                comb = ''.join(sorted(comb))
                if comb in dic:
                    num = dic[comb] + 1
                dic[comb] = num
                mx[c] = max(mx[c], num)
    result = [k for k, v in dic.items() if v != 1 and v == mx[len(k)]]
    return sorted(result)

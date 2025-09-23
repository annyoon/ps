def solution(n, words):
    dic = {}
    for i in range(len(words)):
        if len(words[i]) == 1 or (i > 0 and words[i - 1][-1] != words[i][0]) or words[i] in dic:
            return [i % n + 1, i // n + 1]
        dic[words[i]] = True
    return [0, 0]

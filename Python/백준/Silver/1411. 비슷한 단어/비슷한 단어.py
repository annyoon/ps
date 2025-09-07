N = int(input())
arr = [input() for _ in range(N)]

answer = 0

for i in range(N):
    dic = {}
    word = arr[i]
    compare = []

    for idx in range(len(word)):
        if word[idx] in dic:
            compare.append(dic[word[idx]])
        else:
            dic[word[idx]]= idx
            compare.append(idx)


    for j in range(i + 1, len(arr)):
        dic = {}
        cur = arr[j]
        tmp = []
        flag = False

        for idx in range(len(cur)):
            if cur[idx] in dic:
                tmp.append(dic[cur[idx]])
            else:
                dic[cur[idx]]= idx
                tmp.append(idx)
            if tmp[idx] != compare[idx]:
                flag = True
                break
        if not flag:
            answer += 1

print(answer)

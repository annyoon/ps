from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 10 ** 9

for i in range(1, N + 1):
    results = list(combinations(arr, i))
    for result in results:
        s, b = 1, 0
        for j in range(i):
            s *= result[j][0]
            b += result[j][1]
        answer = min(answer, abs(s - b))

print(answer)

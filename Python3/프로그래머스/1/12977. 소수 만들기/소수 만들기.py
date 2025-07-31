answer = 0

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def getCombinations(nums, start, picked):
    global answer
    
    if len(picked) == 3:
        if isPrime(sum(picked)):
            answer += 1
        return
    
    for i in range(start, len(nums)):
        picked.append(nums[i])
        getCombinations(nums, i + 1, picked)
        picked.pop()

def solution(nums):
    getCombinations(nums, 0, [])
    return answer

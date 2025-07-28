def solution(nums):
    s = set(nums)
    return len(s) if len(s) < len(nums) // 2 else len(nums) // 2
